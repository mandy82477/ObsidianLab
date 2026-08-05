# 任務 × 跨家模型領先者週快照

**狀態：** ongoing
**領域：** 🤖 模型
**更新頻率：** 🗓️ 週更（每週抓取一次外部榜單快照；更新日期停留數天屬正常節奏）
**開始日期：** 2026-08-05
**最後更新：** 2026-08-05
**最後新聞更新：** 2026-08-05

> **本週快照重點**（2026-08-05）
> 寫 code 與對話由 Claude 領先（SWE-bench Verified Opus 5 96%、LMArena Fable 5 ~1525）、畫圖 OpenAI 領先（GPT Image 2）、影片 Google 領先（Gemini Omni Flash）；實際 API 用量榜則由 DeepSeek V4 Flash 等低價 MoE 模型稱王——「最強」與「大家實際在用」是兩個世界。

---

## 摘要

回答「**做某類任務，目前哪家模型最強？**」——按任務類型列出各活榜單的本週領先者快照，涵蓋跨家模型（OpenAI、Google、開源等）與非文字生成（畫圖、影片、語音）。每列標資料日期與取得方式；即時精確數字請點榜單連結（活榜單永遠最新，本頁只是每週速讀）。Claude 家內選型見 [[topics/model-comparison]]。

## 本週快照

| 你想做的任務 | 目前領先者 | 關鍵數字 | 資料日期・方式 | 榜單 |
|---|---|---|---|---|
| 寫 code（agent 解 issue） | Claude Opus 5 | SWE-bench Verified 96%（前三全 Claude） | 08-04・二手報導 | [SWE-bench](https://www.swebench.com/) |
| 寫 code（Aider 實戰） | gpt-5 (high) | 88.0%（⚠️ 榜自 2025-08 未更新，疑停更） | 2025-08・直接 | [Aider Polyglot](https://aider.chat/docs/leaderboards/) |
| 寫文案、聊天、翻譯 | Claude Fable 5 | Elo ~1525（07-12 重新基準化後） | 08-01・二手報導 | [LMArena](https://lmarena.ai/) |
| 查資料（AI 搜尋） | Claude Opus 4-6 Search | Elo 1253，GPT-5.5 Search 1240 居次 | 08-05・直接 | [Search Arena](https://arena.ai/leaderboard) |
| 做網頁／前端 | Claude Opus 5 Max | Elo 1705，Kimi K3 Max 1676 居次 | 08-05・直接 | [WebDev Arena](https://arena.ai/leaderboard) |
| 畫圖（文生圖） | GPT Image 2 (high) | Elo 1339，Reve 2.1 1299 居次 | 08-05・直接 | [AA 圖像榜](https://artificialanalysis.ai/image/leaderboard/text-to-image) |
| 生成影片 | Gemini Omni Flash | Elo 1243，MiniMax H3 1237 居次 | 08-05・直接 | [AA 影片榜](https://artificialanalysis.ai/video/leaderboard/text-to-video) |
| 語音合成（TTS） | 快照待補（下週補抓） | — | — | [AA TTS 榜](https://artificialanalysis.ai/text-to-speech/leaderboard) |
| 語音轉文字（逐字稿） | Fun-Realtime-ASR-preview | 字錯率 1.7%，ElevenLabs Scribe v2 2.2% 居次 | 08-05・直接 | [AA STT 榜](https://artificialanalysis.ai/speech-to-text) |
| 電腦操作 agent | GPT-5.6 Sol | Terminal-Bench 2.1 91.9%，Opus 5 89.1% 居次 | 07~08 月・二手報導 | [Terminal-Bench](https://www.tbench.ai/) |
| 文件解析／OCR | MiniMax M3 | OmniDocBench 綜合 0.916（16 模型中） | 08 月・二手報導 | [OmniDocBench](https://llm-stats.com/benchmarks/omnidocbench-1.5) |
| 音樂生成 | 快照待補（下週補抓） | — | — | [AA Music Arena](https://artificialanalysis.ai/music/leaderboard/vocals) |
| Embedding（自建 RAG） | Gemini Embedding 001 | MTEB 68.32；開放權重首選 Qwen3-Embedding-8B | 04~07 月・二手報導 | [MTEB](https://huggingface.co/spaces/mteb/leaderboard) |
| 大家實際在用什麼 | DeepSeek V4 Flash | OpenRouter 用量第一，腾訊 Hy3 居次 | 08-02・二手報導 | [OpenRouter](https://openrouter.ai/rankings) |

**取得方式說明：** 「直接」＝當週從榜單頁面直接抓取；「二手報導」＝榜單頁為 JS 渲染無法直接抓取，數字來自近期報導彙整，可能有數天延遲——要精確數字請點榜單連結自行查看。

## 快照細節與注意事項

- **SWE-bench**：Verified 子榜前三為 Opus 5（96%）、Mythos 5（95.5%）、Fable 5（95%）；Pro 子榜 Fable 5 80.3%。官方站 JS 渲染抓不到，數字為二手報導拼湊。
- **Aider Polyglot**：榜首仍是 2025-08 的 gpt-5 陣容，一年未見新模型入榜，**疑似停止維護**——參考價值下降，若持續無更新將汰換此列。
- **LMArena**：平台 2026-07-12 重新基準化 Elo（重算 07-01 後投票），前五為 Fable 5、Opus 4.8、GPT-5.5 Pro、GPT-5.5、Gemini 3.1 Pro Preview。
- **電腦操作 agent**：OSWorld 官方站排行表未公開（僅知最佳模型成功率 12.24% vs 人類 72.36%），故本列採 Terminal-Bench；此領域整體離人類水準仍遠。
- **MTEB**：v2 與 v1 分數不可直接比較；多語系榜（MMTEB）第一為騰訊 KaLM-Embedding-Gemma3-12B（72.32，2026-07）。
- **OpenRouter**：用量占比具體數字抓不到（頁面截斷），僅知排名；此榜反映價格敏感的真實流量，與能力榜天然不同溫。

## 相關實體

- Claude 家內選型：[[topics/model-comparison]]
- 各模型深度資訊：[[entities/fable-5]] · [[entities/opus-5]] · [[entities/sonnet-5]]
- 競品動態：[[topics/competitor-landscape]]
