import pandas as pd
import numpy as np
import os

def add_features(df):
    df['SMA_14'] = df['Close'].rolling(window=14).mean()
    df['EMA_14'] = df['Close'].ewm(span=14, adjust=False).mean()
    df['Price_Change'] = df['Close'].pct_change()
    df['Volatility'] = df['Close'].rolling(window=14).std()
    df['RSI_14'] = compute_rsi(df['Close'], window=14)
    df['Bollinger_Mid'] = df['Close'].rolling(window=20).mean()
    df['Bollinger_Std'] = df['Close'].rolling(window=20).std()
    df['Bollinger_High'] = df['Bollinger_Mid'] + 2 * df['Bollinger_Std']
    df['Bollinger_Low'] = df['Bollinger_Mid'] - 2 * df['Bollinger_Std']
    df['Price_Range'] = df['High'] - df['Low']
    df.dropna(inplace=True)
    return df

def compute_rsi(series, window):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

if __name__ == "__main__":
    os.makedirs("data/featured", exist_ok=True)

    # SPY
    spy = pd.read_csv("data/cleaned/spy_stock_cleaned.csv")
    spy = add_features(spy)
    spy.to_csv("data/featured/spy_stock_featured.csv", index=False)
    print(" SPY features saved to data/featured/spy_stock_featured.csv")

    # EUR/USD
    fx = pd.read_csv("data/cleaned/eurusd_fx_cleaned.csv")
    fx = add_features(fx)
    fx.to_csv("data/featured/eurusd_fx_featured.csv", index=False)
    print(" EURUSD features saved to data/featured/eurusd_fx_featured.csv")
