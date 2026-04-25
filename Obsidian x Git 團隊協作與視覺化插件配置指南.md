

本筆記彙整了關於 **Obsidian** 搭配 **Git** 進行協作時的常見問題、Markdown 語法最佳實踐，以及針對圖表/圖片優化的插件方案。

---

## 🛠️ 1. Git 協作與版本控制規範

在使用 Git 進行筆記同步時，應優先考量「衝突預防」與「Diff 清潔度」。

### 1.1 環境配置 (`.gitignore`)

為避免個人 UI 狀態導致頻繁衝突，請務必排除以下檔案：

Bash

```
# 忽略個人化的工作區狀態（含分頁、視窗佈局、摺疊狀態）
.obsidian/workspace.json
.obsidian/workspace-mobile.json

# 系統快取
.DS_Store
Thumbs.db
```

### 1.2 跨平台換行符號控制

建立 `.gitattributes` 確保 Windows 與 Mac 之間的換行符號一致：

Plaintext

```
* text=auto eol=lf
```

---

## 📝 2. Markdown 語法與摺疊建議

### 2.1 摺疊 (Folding) 的選擇

- **不建議使用 HTML `<details>`：**
    
    - 雖然在 GitHub 網頁端可縮放，但在 Obsidian 編輯器內解析不穩定，且會增加原始碼雜訊，增加 Git 衝突風險。
        
- **推薦使用 Obsidian Callouts (折疊式)：**
    
    > [!info]- 點擊展開詳細內容
    > 
    > 這是推薦的折疊方式，既美觀又不影響 Git 追蹤。
    
- **原子化建議：** 若檔案長到需要大量摺疊，應評估將內容拆分為多個小檔案，利用雙向鏈結跳轉。
    

### 2.2 圖片連結規範

- **格式：** 統一使用 `Relative path to file`（相對路徑）。
    
- **路徑：** 圖片須存於儲存庫內（如 `Attachments/` 目錄）並一併提交至 Git。
    

---

## 📊 3. Mermaid 圖表進階應用

### 3.1 基礎 Mermaid 範例

Code snippet

```
graph TD
    A[開始協作] --> B{是否有衝突?}
    B -- 是 --> C[原始碼模式手動合併]
    B -- 否 --> D[同步成功]
```

### 3.2 圖表放大解決方案

由於 Mermaid 預設渲染較小，推薦使用 **Diagram Popup** 插件進行互動式縮放，避免強行修改 CSS。

---

## 🔌 4. 插件組合與問題對接表 (Problem Mapping)

以下為目前配置的插件及其針對協作痛點提供的解決方案：

|**套件名稱**|**解決的問題 (Mapping)**|**協作效益**|
|---|---|---|
|**Git**|同步自動化、版本控制|提供 Auto-Push/Pull，減少忘記更新導致的衝突。|
|**Advanced Tables**|Markdown 表格排版混亂|保持原始碼對齊，使 Git Diff 易於閱讀。|
|**Diagram Popup**|Mermaid 圖表細節看不清|提供彈出式放大鏡，不破壞筆記原始排版。|
|**Image Toolkit**|圖片縮放與細節查看|點擊圖片即可互動式縮放、旋轉與全螢幕。|
|**Mermaid Tools**|Mermaid 語法不熟、撰寫慢|提供視覺化工具列，快速插入節點。|
|**Style Settings**|團隊介面視覺不統一|透過圖形介面同步主題設定，無需手動寫 CSS。|
|**Templater**|筆記結構不一、缺少 Metadata|一鍵插入標準化 YAML 標頭，規範團隊產出。|
|**Image in Editor**|編輯與預覽模式的視覺落差|達成編輯時即看即所得，減少排版錯誤。|

---

## ⚙️ 5. 進階設定：讓圖片也支援彈出放大

若要讓 **Diagram Popup** 插件支援一般圖片（如 `Pasted image`）：

1. 進入 **Diagram Popup** 插件設定。
    
2. 在 **Add New Target** 區塊：
    
    - **Target:** 輸入 `Image`
        
    - **Class Name:** 輸入 `internal-embed`
        
3. 點擊 **Save**。
    

---

## 🚀 6. 同步與安裝指引

- **多倉庫同步：** Obsidian 插件設定是以儲存庫 (Vault) 為單位的。
    
- **團隊配置：** 建議將 `.obsidian/plugins/` 下的 `data.json` 納入 Git 管理，確保每位同仁的插件設定（如放大倍率、Target 清單）完全一致。