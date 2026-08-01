#!/usr/bin/env python3
"""cloud_bootstrap.py — 雲端沙盒的環境自備補丁（冪等，可重複執行）。

雲端 routine 每次都是全新容器，而該環境預設缺三個東西：

  1. `python-dotenv` — `main.py` 匯入鏈的第一步就撞這個
  2. `feedparser`     — 所有 RSS 來源與 blogroll 依賴
  3. `sgmllib3k`      — feedparser 的 legacy 解析路徑依賴，但它用 `setup.py install`
     安裝，在 Python 3.11 會觸發 distutils／setuptools 相容性錯誤
     （`install_layout` AttributeError），導致 wheel build 失敗；連帶讓
     `pip install -r src/requirements_news.txt` 整包裝不起來

繞法（2026-07-14 起每次雲端執行都手動重做一遍，已至少復現 5 次：07-14、07-21、
07-22、07-23、07-24）：跳過 sgmllib3k 壞掉的安裝步驟，直接抓原始碼把 `sgmllib.py`
放進 site-packages。本腳本把那套手動步驟固化下來，讓它跟著 repo 走。

本腳本是 workaround 而非真解：真解是雲端基礎映像預裝這些套件，或上游移除
sgmllib3k 依賴。見 `docs/workaround-register.md` 對應列。

設計原則：
  - **冪等**：已可匯入的套件直接跳過，重跑不會重裝
  - **不致命**：任何一步失敗都只印警告並繼續，退出碼恆為 0。這是輔助腳本，
    不該因為它自己出問題而擋掉整條 pipeline——真正該擋的是後續步驟自己的檢查
  - **只在需要時動手**：本機（Windows）通常三個套件都在，跑起來會是全部跳過

用法：
    python scripts/cloud_bootstrap.py
"""
from __future__ import annotations

import builtins
import importlib.util
import io
import subprocess
import sys
import sysconfig
import tarfile
import tempfile
from pathlib import Path

def _use_utf8_stdout() -> None:
    """Windows 主控台預設 cp950，印不出 ✅／⚠️ 會 UnicodeEncodeError。

    只在直接執行時呼叫，**不可**放在模組層級：模組層級換掉 sys.stdout 會在本檔
    被 import 時連帶關掉呼叫端的輸出流（實際踩過：unittest discover 匯入姊妹腳本
    後噴 `ValueError: I/O operation on closed file`）。
    """
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def print(*args, **kwargs):  # noqa: A001 - 蓋掉內建 print，確保永不因編碼中斷
    try:
        builtins.print(*args, **kwargs)
    except UnicodeEncodeError:
        builtins.print(*(str(a).encode("ascii", "replace").decode() for a in args), **kwargs)

PIP_PACKAGES = [
    ("dotenv", "python-dotenv"),
    # feedparser 6.0.14 起把依賴從壞掉的 sgmllib3k 換成正常出 wheel 的
    # feedparser-sgmllib（見 ensure_pip_packages 說明），所以這裡鎖下界並讓 pip
    # 正常解析依賴，不再 --no-deps
    ("feedparser", "feedparser>=6.0.14"),
]


def _have(module: str) -> bool:
    try:
        return importlib.util.find_spec(module) is not None
    except (ImportError, ValueError):
        return False


def _pip(*args: str) -> bool:
    cmd = [sys.executable, "-m", "pip", *args]
    print(f"  $ {' '.join(cmd[1:])}")
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    except Exception as e:
        print(f"  ⚠️ 執行失敗：{e}")
        return False
    if r.returncode != 0:
        print(f"  ⚠️ pip 回傳 {r.returncode}：{(r.stderr or '').strip()[:400]}")
        return False
    return True


def ensure_pip_packages() -> None:
    """正常安裝（含依賴）。

    2026-08-01 查證：feedparser 6.0.14 已把依賴從壞掉的 `sgmllib3k` 換成
    `feedparser-sgmllib`（純 python wheel、無依賴、requires_python >=3.10），
    乾淨 venv 實測 `pip install feedparser>=6.0.14` 一次成功、`feedparser.sgml`
    可 import、實際 parse 正常。也就是說本檔存在的根因已由上游移除。

    舊版曾用 `--no-deps` 躲開壞掉的 sgmllib3k——那個旗標同時也讓 pip 永遠看不到
    上游換掉依賴這件事，是這個 workaround 遲遲沒退場的直接原因，故一併移除。
    """
    for module, spec in PIP_PACKAGES:
        if _have(module):
            print(f"✅ {spec}：已存在，跳過")
            continue
        print(f"📦 {spec}：缺少，安裝中")
        if _pip("install", spec) and _have(module):
            print(f"✅ {spec}：安裝完成")
        else:
            print(f"⚠️ {spec}：安裝未成功，後續步驟可能失敗")


def ensure_sgmllib() -> None:
    """繞過 sgmllib3k 壞掉的 setup.py：抓原始碼，只把 sgmllib.py 放進 site-packages。"""
    if _have("sgmllib"):
        print("✅ sgmllib：已存在，跳過")
        return

    site = sysconfig.get_paths().get("purelib")
    if not site:
        print("⚠️ sgmllib：找不到 site-packages 路徑，跳過")
        return
    site_dir = Path(site)

    print("📦 sgmllib3k：缺少，改用原始碼安裝（其 setup.py 在 Python 3.11 會壞）")
    with tempfile.TemporaryDirectory() as tmp:
        if not _pip("download", "--no-deps", "--no-binary", ":all:", "-d", tmp, "sgmllib3k"):
            print("⚠️ sgmllib3k：下載失敗，跳過")
            return
        archives = list(Path(tmp).glob("sgmllib3k*.tar.gz"))
        if not archives:
            print(f"⚠️ sgmllib3k：下載目錄中找不到 tar.gz（{[p.name for p in Path(tmp).iterdir()]}）")
            return
        try:
            with tarfile.open(archives[0]) as tf:
                member = next((m for m in tf.getmembers() if Path(m.name).name == "sgmllib.py"), None)
                if member is None:
                    print("⚠️ sgmllib3k：壓縮檔中找不到 sgmllib.py")
                    return
                extracted = tf.extractfile(member)
                if extracted is None:
                    print("⚠️ sgmllib3k：無法讀出 sgmllib.py")
                    return
                (site_dir / "sgmllib.py").write_bytes(extracted.read())
        except Exception as e:
            print(f"⚠️ sgmllib3k：解壓失敗（{e}）")
            return
    print(f"✅ sgmllib：已放入 {site_dir / 'sgmllib.py'}")


def ensure_feedparser_vendored_sgmllib() -> None:
    """feedparser 每隔幾版就換一次 sgmllib 的 vendoring 路徑，同一根因至今已三種症狀：

      - ≤ 6.0.12：`import sgmllib`            → 頂層模組（`ensure_sgmllib()` 負責）
      - 6.0.13：  `import feedparser.sgmllib` → 套件**內部**檔案
      - 6.0.14：  `import feedparser_sgmllib` → 獨立的頂層 distribution package

    逐版追著補會一直在雲端 routine 踩雷（07-28、07-31、08-01 三次復現，見
    docs/workaround-register.md），所以這裡改為**一次把三條路徑全部鋪好**：同一份
    sgmllib.py 分別放到頂層 `sgmllib.py`、`feedparser/sgmllib.py`、
    `feedparser_sgmllib.py`。feedparser 只會 import 自己那版認得的那一條，多出來的
    副本不會被載入，無副作用；日後若上游再換名，只需在 `aliases` 加一行。"""
    if not _have("feedparser"):
        return  # feedparser 本身沒裝好，上面已警告過，這裡不重複

    site = sysconfig.get_paths().get("purelib")
    src = Path(site) / "sgmllib.py" if site else None
    if not src or not src.exists():
        print("⚠️ feedparser sgmllib 別名：找不到頂層 sgmllib.py，跳過")
        return

    try:
        spec = importlib.util.find_spec("feedparser")
        pkg_dirs = list(spec.submodule_search_locations or []) if spec else []
    except (ImportError, ValueError):
        pkg_dirs = []

    # (import 名稱, 目標檔案路徑)
    aliases: list[tuple[str, Path]] = [("feedparser_sgmllib", Path(site) / "feedparser_sgmllib.py")]
    if pkg_dirs:
        aliases.insert(0, ("feedparser.sgmllib", Path(pkg_dirs[0]) / "sgmllib.py"))
    else:
        print("⚠️ feedparser sgmllib 別名：找不到 feedparser 套件目錄，略過套件內路徑")

    for mod_name, dest in aliases:
        if _have(mod_name):
            print(f"✅ {mod_name}：已存在，跳過")
            continue
        try:
            dest.write_bytes(src.read_bytes())
            print(f"✅ {mod_name}：已複製至 {dest}")
        except Exception as e:
            print(f"⚠️ {mod_name}：複製失敗（{e}）")


def verify_feedparser_import() -> bool:
    """真正要的不是「sgmllib 檔案在不在」，而是 `feedparser.sgml` 能不能 import——
    前三次雲端失敗都是「bootstrap 回報依賴就緒、實際 import 仍炸」。這裡直接驗
    真實 import 路徑，讓 bootstrap 的結論與 pipeline 的實際遭遇一致。"""
    importlib.invalidate_caches()
    try:
        importlib.import_module("feedparser.sgml")
        print("✅ feedparser.sgml：import 驗證通過")
        return True
    except Exception as e:
        print(f"⚠️ feedparser.sgml：import 仍失敗（{type(e).__name__}: {e}）")
        return False


def main() -> int:
    _use_utf8_stdout()
    print("=== 雲端環境自備補丁（冪等；本機通常全部跳過）===")
    ensure_pip_packages()

    # 主路徑：上游 6.0.14 起已自備可正常安裝的 sgmllib，正常裝完就該直接通過。
    ok = all(_have(m) for m, _ in PIP_PACKAGES) and verify_feedparser_import()

    if not ok:
        # 退路一：環境預裝了 6.0.14 以前的 feedparser，`_have()` 會判定「已存在」
        # 而不升版，於是又回到舊症狀。這裡明確升上去再驗一次。
        print("↩️ 退路一：嘗試升級 feedparser 至 6.0.14 以上")
        if _pip("install", "--upgrade", "feedparser>=6.0.14"):
            ok = verify_feedparser_import()

    if not ok:
        # 退路二：離線或 PyPI 不可達等情況，退回 2026-07 的手動 vendoring 修法。
        # 保留是因為它是唯一不需要網路裝新套件就能救回來的路；正常情況不會走到。
        print("↩️ 退路二：改用手動 vendoring 修法（sgmllib 三路徑鋪設）")
        ensure_sgmllib()
        ensure_feedparser_vendored_sgmllib()
        ok = verify_feedparser_import()

    print("=== 結果：" + ("依賴皆就緒" if ok else "仍有依賴缺失，後續步驟可能失敗（見上方警告）") + " ===")
    return 0  # 恆為 0：輔助腳本不該擋掉 pipeline


if __name__ == "__main__":
    sys.exit(main())
