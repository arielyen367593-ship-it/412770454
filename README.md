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

## 執行方式
```bash
pip install yfinance mplfinance pandas matplotlib
python main.py
