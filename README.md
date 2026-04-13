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

生成式AI期中/ ├── README.md ├── main.py                  # 主程式（yfinance + mplfinance） ├── tw_stock_analysis.ipynb  # Jupyter Notebook 執行版本 ├── requirements.txt ├── stock_groups.json        # 族群分類設定檔 └── output/                  # 產出圖檔 ├── 半導體製造族群_大盤K線.png ├── AI硬體伺服器族群_大盤K線.png └── 各股票個股K線圖.png


