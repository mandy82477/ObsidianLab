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

# Windows 主控台預設 cp950，印不出 ✅／⚠️ 這類字元會直接 UnicodeEncodeError。
# 本腳本兩邊環境都會跑（雲端 Linux/UTF-8、本機 Windows/cp950），統一把輸出
# 轉成 UTF-8 且遇到無法編碼的字元以替代字元帶過，不讓「印字」搞掛「裝套件」。
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def print(*args, **kwargs):  # noqa: A001 - 蓋掉內建 print，確保永不因編碼中斷
    try:
        builtins.print(*args, **kwargs)
    except UnicodeEncodeError:
        builtins.print(*(str(a).encode("ascii", "replace").decode() for a in args), **kwargs)

PIP_PACKAGES = [
    ("dotenv", "python-dotenv"),
    ("feedparser", "feedparser"),
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
    for module, dist in PIP_PACKAGES:
        if _have(module):
            print(f"✅ {dist}：已存在，跳過")
            continue
        print(f"📦 {dist}：缺少，安裝中")
        # --no-deps：feedparser 會把壞掉的 sgmllib3k 拉進來一起裝而整包失敗，
        # sgmllib3k 交給下面的專用流程處理
        if _pip("install", "--no-deps", dist) and _have(module):
            print(f"✅ {dist}：安裝完成")
        else:
            print(f"⚠️ {dist}：安裝未成功，後續步驟可能失敗")


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


def main() -> int:
    print("=== 雲端環境自備補丁（冪等；本機通常全部跳過）===")
    ensure_pip_packages()
    ensure_sgmllib()
    ok = all(_have(m) for m, _ in PIP_PACKAGES) and _have("sgmllib")
    print("=== 結果：" + ("三個依賴皆就緒" if ok else "仍有依賴缺失，後續步驟可能失敗（見上方警告）") + " ===")
    return 0  # 恆為 0：輔助腳本不該擋掉 pipeline


if __name__ == "__main__":
    sys.exit(main())
