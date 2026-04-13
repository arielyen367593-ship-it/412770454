# Vibe Coding - 台股分析

生成式 AI 期中分組報告  
**完全使用 AI 完成所有任務**

## 專案目標
- 蒐集台股每日 OHLC 資料
- 研究半導體 / AI 類股並分類（每類 ≤5 檔）
- 製作每個分類的大盤 K 線圖
- 專業趨勢分析

## 使用 AI 工具鏈
- 主要 AI：Grok (xAI) —— 所有研究、分類、程式碼產生、分析
- 開發環境：Python 3 + Jupyter Notebook + Anaconda
- 資料來源：yfinance



- ---

### 執行環境
- **Python**：3.10+
- **pandas**：資料清理與等權重指數計算
- **yfinance**：從 Yahoo Finance API 抓取真實台股 OHLCV 資料
- **mplfinance**：專業 K 線圖繪製（個股使用 candle，族群大盤使用 line）
- **開發環境**：Windows + Anaconda + Jupyter Notebook

---

3. 程式生成與修正
•  使用 Grok (xAI) 協助撰寫資料下載與 K 線圖繪製程式
•  針對執行過程中遇到的 5 大類錯誤（套件、資料型態、yfinance bug、圖表顯示等）反覆修正 Prompt 與程式碼
•  將趨勢判讀邏輯直接整合進輸出流程
4. AI 協助圖表分析
•  由 AI 根據 K 線圖與技術指標生成初步分析文字
•  人工確認內容正確性後，整理成報告可直接使用的段落
5. 文件撰寫
•  使用 AI 協助產生 README.md、報告大綱與口頭講稿
•  人工統一語氣與內容結構

本專案的價值
這份作業不只是畫出 K 線圖，而是完整展示：
•  如何把模糊需求拆成可執行步驟
•  如何用 AI 加速資料分析專案
•  如何驗證 AI 生成結果
•  如何讓 AI 協助讀圖並產出可用分析文字
•  如何產出具備 GitHub 可讀性的完整專案

Future Work
•  加入成交量與技術指標（MA、MACD、RSI）
•  自動輸出 PDF 報告與圖表摘要
•  將多張圖整合成互動式 Dashboard
•  加入族群比較統計表與強弱排名分析

### 執行方式
執行後程式會自動完成以下流程：
1. 讀取預設股票分類（半導體製造族群、AI硬體伺服器族群）
2. 下載每檔股票最近兩年的歷史資料
3. 輸出各股票標準 K 線圖（含成交量）
4. 計算族群等權重大盤指數並輸出線型 K 線圖
5. 對個股與族群圖表進行趨勢判讀
6. 將所有圖檔與分析結果輸出至 `output/` 資料夾

```bash
pip install -r requirements.txt
python main.py

- ### 專案結構

生成式AI期中/
├── README.md                    # 本檔案（專案說明）
├── main.py                      # 主程式（yfinance + mplfinance）
├── tw_stock_analysis.ipynb      # Jupyter Notebook 互動版本
├── requirements.txt             # 所需套件清單
├── stock_groups.json            # 股票分類設定檔
└── output/                      # 所有產出圖檔
    ├── 半導體製造族群_大盤K線.png
    ├── AI硬體伺服器族群_大盤K線.png
    ├── 2330.TW_K線圖.png
    ├── 2303.TW_K線圖.png
    ├── 3711.TW_K線圖.png
    ├── 2454.TW_K線圖.png
    ├── 6669.TW_K線圖.png
    ├── 2317.TW_K線圖.png
    ├── 2382.TW_K線圖.png
    └── 2308.TW_K線圖.png


```bash

## 執行方式
```bash
pip install yfinance mplfinance pandas matplotlib
python 

