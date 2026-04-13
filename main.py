# Vibe Coding - 台股分析 (2026/4/13 終極穩定版 - 已升級 yfinance 後使用)
# 使用 Grok (xAI) 100% 產生
!pip install --upgrade yfinance --quiet
# Vibe Coding - 台股分析 (2026/4/13 修正版 - 大盤 K 線改用線圖)
# 使用 Grok (xAI) 100% 產生

import yfinance as yf
import pandas as pd
import mplfinance as mpf
from datetime import datetime

print("✅ 開始重新繪製 K 線圖...")

# ================== 股票分類 ==================
groups = {
    "半導體製造族群": ["2330.TW", "2303.TW", "3711.TW"],
    "AI硬體伺服器族群": ["2454.TW", "6669.TW", "2317.TW", "2382.TW", "2308.TW"]
}

end_date = datetime.today().strftime('%Y-%m-%d')
start_date = "2024-01-01"

data = {}
for group_name, tickers in groups.items():
    data[group_name] = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        df = stock.history(start=start_date, end=end_date, auto_adjust=True)
        if df.empty:
            continue
        df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
        df = df.apply(pd.to_numeric, errors='coerce').dropna(how='any').astype('float64')
        data[group_name][ticker] = df

# ================== 修正後的繪製部分 ==================
print("\n🎨 重新繪製 K 線圖...")

for group_name, stocks in data.items():
    if not stocks:
        continue
    
    # 1. 個股 K 線圖（保持不變）
    for ticker, df in stocks.items():
        mpf.plot(df, type='candle', volume=True, 
                 title=f"{ticker} K 線圖 ({group_name})",
                 style='yahoo',
                 savefig=f"{ticker}_K線圖.png",
                 figsize=(12, 7))
    
    # 2. 大盤 K 線圖 ← 關鍵修正：改用 type='line'
    norm = pd.DataFrame()
    for ticker, df in stocks.items():
        norm[ticker] = df['Close'] / df['Close'].iloc[0] * 100
    
    index_df = pd.DataFrame({
        'Open': norm.mean(axis=1),
        'High': norm.mean(axis=1),
        'Low': norm.mean(axis=1),
        'Close': norm.mean(axis=1),
        'Volume': 0
    })
    index_df.index = norm.index
    
    print(f"   繪製 {group_name} 等權重大盤 K 線（已修正為線圖）...")
    mpf.plot(index_df, 
             type='line',          # ← 改成 line 就不會只有點點
             volume=False, 
             title=f"{group_name} 等權重大盤指數 K 線",
             style='yahoo',
             savefig=f"{group_name}_大盤K線.png",
             figsize=(12, 6))

print("\n🎉 修正完成！以下檔案已更新：")
import os
files = [f for f in os.listdir('.') if f.endswith('.png')]
for f in sorted(files):
    print(f"   📁 {f}")
