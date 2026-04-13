pip install yfinance mplfinance pandas matplotlib
# Vibe Coding - 台股分析 (2026/4/13 最終終極版 - 徹底解決數據型態)
# 使用 Grok (xAI) 100% 產生

# ================== 自動安裝必要套件 ==================
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])

print("🔧 正在安裝必要套件...")
install("yfinance")
install("mplfinance")
install("pandas")
install("matplotlib")

# ================== 開始正式程式 ==================
import yfinance as yf
import pandas as pd
import mplfinance as mpf
from datetime import datetime
import numpy as np

print("✅ 套件安裝完成！開始下載台股資料...")

# ================== 股票分類 ==================
groups = {
    "半導體製造族群": ["2330.TW", "2303.TW", "3711.TW"],
    "AI硬體伺服器族群": ["2454.TW", "6669.TW", "2317.TW", "2382.TW", "2308.TW"]
}

# 下載期間
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = "2024-01-01"

data = {}
for group_name, tickers in groups.items():
    data[group_name] = {}
    for ticker in tickers:
        print(f"下載 {ticker} 資料...")
        try:
            df = yf.download(ticker, start=start_date, end=end_date, progress=False, auto_adjust=True)
            
            if df.empty:
                print(f"⚠️ {ticker} 無資料")
                continue
            
            # === 徹底的數據清理 ===
            df = df[['Open', 'High', 'Low', 'Close', 'Volume']].copy()
            
            # 1. 轉換為數字型態（遇到非數字轉為 NaN）
            for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            
            # 2. 移除有任何 NaN 的行
            df = df.dropna(how='any')
            
            # 3. 強制轉換為 float64（確保 mplfinance 可接受）
            df[['Open', 'High', 'Low', 'Close']] = df[['Open', 'High', 'Low', 'Close']].astype('float64')
            df['Volume'] = df['Volume'].astype('int64')
            
            # 4. 確保索引是 datetime
            if not isinstance(df.index, pd.DatetimeIndex):
                df.index = pd.to_datetime(df.index)
            
            # 5. 排序並驗證
            df = df.sort_index()
            
            # 最後驗證：檢查是否有 NaN 或無限值
            if df.isnull().any().any() or np.isinf(df[['Open', 'High', 'Low', 'Close']]).any().any():
                print(f"⚠️ {ticker} 包含 NaN 或無限值，跳過")
                continue
            
            if df.empty:
                print(f"⚠️ {ticker} 清理後無有效資料")
                continue
            
            data[group_name][ticker] = df
            print(f"   ✅ {ticker} 成功 | 資料筆數: {len(df)} | 型態: O={df['Open'].dtype}, V={df['Volume'].dtype}")
            
        except Exception as e:
            print(f"❌ {ticker} 錯誤: {str(e)}")
            continue

# ================== 繪製 K 線圖 ==================
print("\n🎨 開始繪製 K 線圖...")

for group_name, stocks in data.items():
    if not stocks:
        print(f"⚠️ {group_name} 無可用資料，跳過")
        continue
    
    print(f"\n📊 處理 {group_name} ...")
    
    # 1. 個股 K 線圖（每一檔單獨存檔，更穩定）
    for ticker, df in stocks.items():
        print(f"   繪製 {ticker} 個股 K 線...")
        
        try:
            mpf.plot(df, 
                     type='candle', 
                     volume=True, 
                     title=f"{ticker} K 線圖 ({group_name})",
                     style='yahoo',
                     savefig=f"{ticker}_K線圖.png",
                     figsize=(12, 7))
        except Exception as e:
            print(f"   ❌ {ticker} 繪圖失敗: {str(e)}")
    
    # 2. 等權重大盤指數 K 線（報告主圖）
    try:
        norm = pd.DataFrame()
        for ticker, df in stocks.items():
            norm[ticker] = df['Close'] / df['Close'].iloc[0] * 100
        
        index_df = pd.DataFrame({
            'Open': norm.mean(axis=1),
            'High': norm.mean(axis=1),
            'Low': norm.mean(axis=1),
            'Close': norm.mean(axis=1),
            'Volume': pd.Series(np.zeros(len(norm)), index=norm.index, dtype='int64')
        })
        index_df.index = norm.index
        
        print(f"   繪製 {group_name} 等權重大盤 K 線...")
        mpf.plot(index_df, 
                 type='candle', 
                 volume=False, 
                 title=f"{group_name} 等權重大盤指數 K 線",
                 style='yahoo',
                 savefig=f"{group_name}_大盤K線.png",
                 figsize=(12, 6))
    except Exception as e:
        print(f"   ❌ {group_name} 大盤圖繪製失敗: {str(e)}")

print("\n🎉 全部完成！以下檔案已儲存：")
import os
files = [f for f in os.listdir('.') if f.endswith('.png')]
for f in sorted(files):
    print(f"   📁 {f}")

print("\n✅ 報告用的 2 張大盤 K 線圖已產生，直接插入 PDF 即可！")
