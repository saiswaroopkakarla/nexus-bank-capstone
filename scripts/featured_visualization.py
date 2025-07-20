import pandas as pd
import matplotlib.pyplot as plt
import os

# Output folder
OUTPUT_FOLDER = "outputs/plots"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load featured datasets
spy_df = pd.read_csv("data/featured/spy_stock_featured.csv")
eurusd_df = pd.read_csv("data/featured/eurusd_fx_featured.csv")

# Convert 'Date' column to datetime
spy_df["Date"] = pd.to_datetime(spy_df["Date"])
eurusd_df["Date"] = pd.to_datetime(eurusd_df["Date"])

# Indicators for individual plots
indicators = {
    "SMA_14": "Simple Moving Average (14)",
    "EMA_14": "Exponential Moving Average (14)",
    "RSI_14": "Relative Strength Index (14)",
    "Volatility": "Volatility (Std Dev)",
    "Price_Change": "Price Change (%)"
}

# Plot individual indicators
def plot_indicator(df, asset_name, column, label):
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df[column], label=label, color="blue")
    plt.title(f"{asset_name} - {label}")
    plt.xlabel("Date")
    plt.ylabel(label)
    plt.grid(True)
    plt.tight_layout()

    save_name = f"{OUTPUT_FOLDER}/{asset_name.lower()}_{column.lower()}.png"
    plt.savefig(save_name)
    plt.close()
    print(f" Saved plot: {save_name}")

# Plot Bollinger Bands (High, Mid, Low in one plot)
def plot_bollinger_bands(df, asset_name):
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Bollinger_High"], label="Bollinger High", color="red", linestyle="--")
    plt.plot(df["Date"], df["Bollinger_Mid"], label="Bollinger Mid", color="black")
    plt.plot(df["Date"], df["Bollinger_Low"], label="Bollinger Low", color="green", linestyle="--")

    plt.title(f"{asset_name} - Bollinger Bands (High, Mid, Low)")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    save_name = f"{OUTPUT_FOLDER}/{asset_name.lower()}_bollinger_bands.png"
    plt.savefig(save_name)
    plt.close()
    print(f" Saved plot: {save_name}")

if __name__ == "__main__":
    for col, label in indicators.items():
        if col in spy_df.columns:
            plot_indicator(spy_df, "SPY", col, label)
        if col in eurusd_df.columns:
            plot_indicator(eurusd_df, "EURUSD", col, label)

    # Bollinger Band Plots
    plot_bollinger_bands(spy_df, "SPY")
    plot_bollinger_bands(eurusd_df, "EURUSD")

    print("\n All plots including Bollinger Bands saved in outputs/plots/")
