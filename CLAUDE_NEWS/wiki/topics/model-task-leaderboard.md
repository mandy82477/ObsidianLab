---
page: "topics/model-task-leaderboard"
kind: "topic"
status: "ongoing"
domain: "🤖 模型"
last_updated: "2026-08-05"
last_news_update: "2026-08-05"
update_freq: "🗓️ 週更（每週抓取一次外部榜單快照；更新日期停留數天屬正常節奏）"
status_main: "ongoing"
days_since_news: 0
inbound_links: 1
attribution_count: 0
attribution_last: null
top_source: null
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
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

| 你想做的任務 | 本週前三名 | 資料日期 | 榜單 |
|---|---|---|---|
| 寫 code（agent 解 issue） | Claude Opus 5 > Mythos 5 > Fable 5 | 08-04 | [SWE-bench](https://www.swebench.com/) |
| 寫 code（Aider 實戰） | gpt-5 (high) > gpt-5 (medium) > o3-pro（⚠️ 榜疑停更） | 2025-08 | [Aider Polyglot](https://aider.chat/docs/leaderboards/) |
| 寫文案、聊天、翻譯 | Claude Fable 5 > Opus 4.8 > GPT-5.5 Pro | 08-01 | [LMArena](https://lmarena.ai/) |
| 查資料（AI 搜尋） | Claude Opus 4-6 Search > GPT-5.5 Search > Fable 5 | 08-05 | [Search Arena](https://arena.ai/leaderboard) |
| 做網頁／前端 | Claude Opus 5 Max > Kimi K3 Max > Opus 5 High | 08-05 | [WebDev Arena](https://arena.ai/leaderboard) |
| 畫圖（文生圖） | GPT Image 2 > Reve 2.1 > MAI-Image-2.5 | 08-05 | [AA 圖像榜](https://artificialanalysis.ai/image/leaderboard/text-to-image) |
| 生成影片 | Gemini Omni Flash > MiniMax H3 > Seedance 2.0 | 08-05 | [AA 影片榜](https://artificialanalysis.ai/video/leaderboard/text-to-video) |
| 語音合成（TTS） | 快照待補（下週補抓） | — | [AA TTS 榜](https://artificialanalysis.ai/text-to-speech/leaderboard) |
| 語音轉文字（逐字稿） | Fun-Realtime-ASR > Scribe v2 > MAI-Transcribe-1.5 | 08-05 | [AA STT 榜](https://artificialanalysis.ai/speech-to-text) |
| 電腦操作 agent | GPT-5.6 Sol > Claude Opus 5 > Mythos 5 | 07~08 月 | [Terminal-Bench](https://www.tbench.ai/) |
| 文件解析／OCR | MiniMax M3（其餘排名未公開） | 08 月 | [OmniDocBench](https://llm-stats.com/benchmarks/omnidocbench-1.5) |
| 音樂生成 | 快照待補（下週補抓） | — | [AA Music Arena](https://artificialanalysis.ai/music/leaderboard/vocals) |
| Embedding（自建 RAG） | Gemini Embedding 001 > Voyage-3.1 > Cohere embed-v4 | 04~07 月 | [MTEB](https://huggingface.co/spaces/mteb/leaderboard) |
| 聊天陪伴／情商 | Claude Fable 5 > Kimi K3 > GPT-5.5 | 07-20 | [EQ-Bench](https://eqbench.com/) |
| 放多長的任務給 agent | Claude Opus 4.5 > GPT-5 > o3（⚠️ 量測落後現役陣容） | 2026-01 | [METR](https://metr.org/) |
| 讀文件不胡說（幻覺率低） | finix_s1_32b > gpt-5.4-nano > gemini-2.5-flash-lite | 05-11 | [Vectara 幻覺榜](https://github.com/vectara/hallucination-leaderboard) |
| 大家實際在用什麼 | DeepSeek V4 Flash > 腾訊 Hy3 > GPT 5.6 Luna | 08-02 | [OpenRouter](https://openrouter.ai/rankings) |

## 快照細節與注意事項

具體分數、取得方式（當週直接抓取或二手報導彙整）與逐榜注意事項如下；要即時精確數字請點表中榜單連結。

- **SWE-bench**（二手報導）：Verified 子榜 Opus 5 96%、Mythos 5 95.5%、Fable 5 95%；Pro 子榜 Fable 5 80.3%。官方站 JS 渲染抓不到，數字為報導拼湊。
- **Aider Polyglot**（直接抓取）：gpt-5 (high) 88.0%、gpt-5 (medium) 86.7%、o3-pro 84.9%——榜首仍是 2025-08 陣容，一年未見新模型入榜，**疑似停止維護**，若持續無更新將汰換此列。
- **LMArena 文字榜**（二手報導）：Fable 5 Elo ~1525、Opus 4.8 ~1510、GPT-5.5 Pro ~1510；平台 2026-07-12 重新基準化 Elo（重算 07-01 後投票）。
- **Search Arena**（直接抓取）：Opus 4-6 Search 1253、GPT-5.5 Search 1240、Fable 5 1237。
- **WebDev Arena**（直接抓取）：Opus 5 Max 1705、Kimi K3 Max 1676、Opus 5 High 1669。
- **畫圖**（直接抓取）：GPT Image 2 (high) Elo 1339、Reve 2.1 1299、MAI-Image-2.5 1270。
- **影片**（直接抓取）：Gemini Omni Flash Elo 1243、MiniMax H3 1237、Dreamina Seedance 2.0 1224。
- **語音轉文字**（直接抓取）：字錯率 Fun-Realtime-ASR-preview 1.7%、ElevenLabs Scribe v2 2.2%、MAI-Transcribe-1.5 2.4%。
- **電腦操作 agent**（二手報導）：Terminal-Bench 2.1 上 GPT-5.6 Sol 91.9%、Opus 5 89.1%、Mythos 5 88.0%。OSWorld 官方站排行表未公開（僅知最佳模型 12.24% vs 人類 72.36%），故採 Terminal-Bench；此領域整體離人類水準仍遠。
- **文件解析／OCR**（二手報導）：OmniDocBench 綜合 MiniMax M3 0.916（16 模型中），其餘排名未公開。
- **Embedding**（二手報導）：MTEB 英文榜 Gemini Embedding 001 68.32、Voyage-3.1 ~67、Cohere embed-v4 65.2；開放權重首選 Qwen3-Embedding-8B（~75）；多語系榜第一為騰訊 KaLM-Embedding-Gemma3-12B（72.32，2026-07）。v2 與 v1 分數不可直接比較。
- **OpenRouter**（二手報導）：用量占比具體數字抓不到（頁面截斷），僅知排名；此榜反映價格敏感的真實流量，與能力榜天然不同溫。
- **METR time horizon**（直接抓取）：非傳統排行榜，量測「50% 成功率下模型可自主完成的任務時長（換算人類工時）」——Time Horizon 1.1（2026-01-29）：Claude Opus 4.5 320 分鐘（信心區間 170–729）、GPT-5 214 分鐘、o3 121 分鐘。此即「agent 自主時長每 7 個月翻倍」曲線的最新公開量測點；**現役陣容（Fable 5 / Opus 5）尚未入測**，數字僅供尺度感，待 METR 下次發布更新。
- **幻覺率**（直接抓取）：Vectara 摘要任務幻覺榜（05-11）：antgroup finix_s1_32b 1.8%、gpt-5.4-nano 3.1%、gemini-2.5-flash-lite 3.3%。注意榜首是螞蟻集團的 32B 小模型——**主流旗艦不必然低幻覺**，選「拿來讀文件／摘要」的模型時，看此榜比看能力榜實用。
- **情商／個性**（二手報導）：EQ-Bench 4 主榜 Fable 5 1349.5、Kimi K3 1349.2、GPT-5.5 1325.8；Creative Writing 子榜第一為 Claude Opus 5（2430）。⚠️ 另一鏡像站（llm-stats，08 月）稱榜首為 Grok 4.1 Thinking（1586），與本輪 BenchLM 快照（07-20）不一致，疑為不同快照日期或子榜版本，待直抓官方站核實。情商高分有「靠討好刷分」的已知疑慮（共情與諂媚同源），解讀時留意。

## 相關實體

- Claude 家內選型：[[topics/model-comparison]]
- 各模型深度資訊：[[entities/fable-5]] · [[entities/opus-5]] · [[entities/sonnet-5]]
- 競品動態：[[topics/competitor-landscape]]
