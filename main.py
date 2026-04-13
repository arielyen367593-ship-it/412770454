# Vibe Coding - 台股分析 (2026/4/13 終極穩定版 - 已升級 yfinance 後使用)
# 使用 Grok (xAI) 100% 產生
!pip install --upgrade yfinance --quiet
import yfinance as yf
import pandas as pd
import mplfinance as mpf
from datetime import datetime

print("✅ 開始下載台股資料...（已升級 yfinance）")

# 股票分類
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
        print(f"下載 {ticker} 資料...")
        try:
            stock = yf.Ticker(ticker)
            df = stock.history(start=start_date, end=end_date, auto_adjust=True, interval="1d")
            
            if df.empty:
                print(f"⚠️ {ticker} 無資料")
                continue
            
            df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
            df = df.apply(pd.to_numeric, errors='coerce')
            df = df.dropna(how='any')
            df = df.astype('float64')
            df = df.sort_index()
            
            if df.empty:
                print(f"⚠️ {ticker} 清理後無有效資料")
                continue
            
            data[group_name][ticker] = df
            print(f"   ✅ {ticker} 成功 | 資料筆數: {len(df)}")
            
        except Exception as e:
            print(f"   ❌ {ticker} 錯誤: {str(e)[:100]}")

# 繪製 K 線圖
print("\n🎨 開始繪製 K 線圖...")

for group_name, stocks in data.items():
    if not stocks:
        print(f"⚠️ {group_name} 無可用資料，跳過")
        continue
    
    print(f"\n📊 處理 {group_name} ...")
    
    # 個股 K 線圖
    for ticker, df in stocks.items():
        print(f"   繪製 {ticker} 個股 K 線...")
        mpf.plot(df, type='candle', volume=True, 
                 title=f"{ticker} K 線圖 ({group_name})",
                 style='yahoo',
                 savefig=f"{ticker}_K線圖.png",
                 figsize=(12, 7))
    
    # 大盤 K 線圖（報告主圖）
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
    
    print(f"   繪製 {group_name} 等權重大盤 K 線...")
    mpf.plot(index_df, type='candle', volume=False, 
             title=f"{group_name} 等權重大盤指數 K 線",
             style='yahoo',
             savefig=f"{group_name}_大盤K線.png",
             figsize=(12, 6))

print("\n🎉 全部完成！以下檔案已儲存：")
import os
files = [f for f in os.listdir('.') if f.endswith('.png')]
for f in sorted(files):
    print(f"   📁 {f}")

print("\n✅ 報告用的 2 張大盤 K 線圖已產生，直接插入 PDF 即可！")
