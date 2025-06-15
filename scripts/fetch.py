import yfinance as yf
import pandas as pd
import os
import logging
from datetime import datetime

# Create logs directory if not exists
os.makedirs("logs", exist_ok=True)

# Format log filename with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"logs/data_fetch_{timestamp}.log"

# Configure logging
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_stock_data(ticker, start, end, save_path):
    logging.info(f"Started downloading data for {ticker}")
    try:
        df = yf.download(ticker, start=start, end=end)
        df.to_csv(save_path)
        logging.info(f"Successfully saved {ticker} data to {save_path}")
        print(f" Data for {ticker} saved to {save_path}")
        return df
    except Exception as e:
        logging.error(f"Failed to fetch data for {ticker}: {e}")
        print(f" Error fetching data for {ticker}")
        return None

if __name__ == "__main__":
    data_folder = "data/raw"
    os.makedirs(data_folder, exist_ok=True)

    fetch_stock_data("SPY", start="2020-01-01", end="2024-12-31", save_path=f"{data_folder}/spy_stock.csv")
    fetch_stock_data("EURUSD=X", start="2020-01-01", end="2024-12-31", save_path=f"{data_folder}/eurusd_fx.csv")
