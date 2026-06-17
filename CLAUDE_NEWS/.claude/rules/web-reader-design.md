# Web Reader 設計規範

修改 `web_reader/index.html`、`web_reader/assets/design.css`、`web_reader/assets/app.js` 前必須讀取此檔案。

---

## 設計語言

**風格：** paper/sumi editorial — 書卷氣排版，hairline 邊框，單一 ochre 強調色。

**三條核心原則：**
1. Hairline-first：邊框用 0.5–1px，不用粗框或填色背景（active 狀態改用 outline 或底線）
2. Sharp corners：`border-radius` ≤ 2px（特例：pill shape 用 `border-radius: 99px`，需有明確理由）
3. 單色強調：全站只有 ochre 一個品牌色，不引入第二強調色

---

## 色票 token（明暗雙模式自動切換）

| token | 用途 |
|-------|------|
| `--ochre-9` | 主強調色（文字、active 狀態、連結 hover） |
| `--ochre-7` | 次要強調（邊框 hover、icon） |
| `--ochre-5` | 輔助 hover（底線、淡色填充） |
| `--ochre-tint` | 背景淡染（active 狀態 bg） |
| `--ink-1` | 主文字 |
| `--ink-2` | 次要文字 |
| `--ink-3` | 輔助文字（placeholder、label） |
| `--ink-4` | 極淡文字（disabled、裝飾） |
| `--bg-0` | 頁面底色（paper 色） |
| `--bg-1` | hover 狀態背景 |
| `--border-2` | 標準邊框（hairline，半透明） |
| `--border-strong` | 強調邊框 |

---

## 字型使用原則

| 變數 | 字型 | 用途 |
|------|------|------|
| `--font-display` | Cormorant Garamond + Noto Serif | 標題、引言、summary 斜體 |
| `--font-sans` | Inter + Noto Sans TC | UI 元件（按鈕、label、chip、nav） |
| `--font-mono` | JetBrains Mono | code、slug、日期、meta 數值 |

**判斷原則：** UI 控制元件（按鈕、chip、filter）用 `--font-sans`；不可用 `--font-mono` 做 UI 控制元件。

---

## 元件慣例

### Tab / filter bar
```css
.tab-row { border-bottom: 1px solid var(--border-2); display: flex; gap: 0; }
.tab {
  font-family: var(--font-sans); font-size: 12px;
  padding: 7px 14px; border-bottom: 2px solid transparent;
  background: transparent; color: var(--ink-3);
  margin-bottom: -1px;
}
.tab:hover { color: var(--ink-2); border-bottom-color: var(--ochre-5); }
.tab--active { color: var(--ochre-9); border-bottom-color: var(--ochre-9); font-weight: 500; }
```

### Pill（狀態標籤）
- border + 文字色，**無填色背景**
- `border-radius: var(--radius-2)`（約 3–4px）
- `.pill--active`：`color: var(--success); border-color: var(--success)`

### 圖示
- 優先使用 inline SVG（自繪，stroke 風格，`stroke-width: 1.8`）
- **不使用平台 emoji 作為 UI 圖示**（跨平台渲染不一致）
- emoji 只允許在 markdown 內文或 wiki 資料值中保留
- icon 尺寸：UI 行內 13px，裝飾性最大 18px

### 卡片（entity / pinned）
- `border: 1px solid var(--border-2)`，`border-radius: 2px`
- hover：`background: var(--bg-1); border-color: var(--border-strong)`
- **無 box-shadow、無 gradient**

---

## 禁止清單

- ❌ gradient（background 和 border 都不行）
- ❌ box-shadow（除非是 focus ring）
- ❌ 平台 emoji 作為 UI 圖示
- ❌ `--font-mono` 用在 UI 控制元件
- ❌ 第二強調色（只有 ochre）
- ❌ `border-radius` > 99px（pill）或 > 2px（其他元件）
- ❌ `font-weight` > 500

---

## 版本號更新

每次修改 `design.css` 或 `app.js` 後，更新 `index.html` 中對應的 `?v=` 參數為當前 Unix timestamp，避免瀏覽器 cache 舊版本。

---

## 修改後必做

1. 確認 JS 中 class selector（如 `.domain-chip--active`、`data-domain`）與 HTML 一致
2. 若新增 CSS class，同步確認無與既有 class 命名衝突
