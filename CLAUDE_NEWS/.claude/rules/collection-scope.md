---
paths:
  - "src/news_aggregator/**"
  - "src/news_aggregator/sources/topic_watch.json"
---
# 蒐集範圍與目標讀者

新增／修改 source、調整收錄門檻、改日報選材規則時讀此檔。

**判斷標準（唯一判準）：**
> 這份資料能幫助**需要深度與穩定資訊的工程師**更了解 Claude / Anthropic 生態系嗎？若否，不收錄。

---

## 目標讀者

- **Claude Code 重度使用者**：想第一時間知道有什麼壞了、值不值得升版，不用自己刷 HN。
- **AI 系統開發者**：在建 agent 或工作流，想知道社群驗證了什麼、踩過哪些坑。
- **Anthropic 生態追蹤者**：關注政策、融資、合作動態，一站掌握生態走向。

## 蒐集範圍

| 類型 | 內容 |
|------|------|
| **官方核心** | GitHub Changelog、SDK / API 迭代、定價結構變化、Anthropic 公告 |
| **社群實測** | 工程師驗證過的工作流模式、agent 設計、Bug 回報與替代方案（HN / Reddit） |
| **生態動態** | 融資、大型企業合作（AWS / Google）、政策趨勢、周邊工具 |
| **專頁定向** | 為特定 wiki 專頁定向抓取的少量條目（`src/news_aggregator/sources/topic_watch.json`），判準是「對該專頁有無價值」而非標題是否提及 Claude／Anthropic |
| **存量盤點** | 已成名但本庫從未報導過的 GitHub repo，每日至多 2 則補進（`src/news_aggregator/sources/github_releases.py` C 窗）。含 Agent Skills 生態——SKILL.md 是 Anthropic originated 的格式，該生態整體屬 Claude 生態，但多數 repo 的描述不含 claude 字樣 |
| **使用者提問** `[加入: 2026-09-02]` | 使用者在對話中點名的事實（工具、事件、疑問），**經主編以 web 工具查證一手來源後**直接沉澱進 wiki，不經日報。紀律：查證是入場券（未查證只能標懸置）、寫入必標「查證日＋來源連結」、歸因 slug `user-query`、`wiki/log.md` Query 條目為溯源記錄。此通道證據等級不低於日報——入口即主編查證，記者通道反而無 web 工具 |

## 不收錄

- X / Discord 即時訊號（社交平台秒級爆料；26–30 小時延遲是設計取捨，非缺陷）
- NDA 保護下的企業非公開資訊
- 與 Claude / Anthropic 無直接關聯的通用 AI 新聞（**例外**：wiki 專頁定向抓取，見上表「專頁定向」——該通道有數量上限且在日報獨立成區，不混入正文六區塊）
- Agent Skills 生態以外、與 Claude 無關的 agent 工具存量（存量盤點通道綁定四條 scope，不是通用 GitHub 熱門榜；scope 清單見 `src/news_aggregator/sources/github_releases.py` 的 `_INVENTORY_SCOPES`）
- 無技術內容的純行銷稿

## 新增來源的做法

繼承 `BaseSource`，實作 `fetch() -> list[FeedItem]`，在 `src/news_aggregator/main.py` 的 `sources` 列表加入即可。來源特性補丁（互動門檻、可比性註記）住 `data/source_registry.json`，不寫進規則檔。
