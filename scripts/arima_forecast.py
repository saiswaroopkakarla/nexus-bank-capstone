import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import os
import warnings
warnings.filterwarnings("ignore")

def arima_forecast(csv_path, asset_name, save_prefix):
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df = df.asfreq('D')  # Ensure daily frequency
    df['Close'] = df['Close'].interpolate()  # Fill missing days

    # Fit ARIMA model
    model = ARIMA(df['Close'], order=(5, 1, 0))
    model_fit = model.fit()

    # Forecast next 30 days
    forecast = model_fit.forecast(steps=30)
    forecast_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=30)

    forecast_df = pd.DataFrame({'Date': forecast_dates, 'Forecast_Close': forecast})
    forecast_df.to_csv(f"data/forecast/{save_prefix}_forecast.csv", index=False)

    # Plot
    plt.figure(figsize=(12,6))
    plt.plot(df.index[-90:], df['Close'][-90:], label="Actual", color="blue")
    plt.plot(forecast_dates, forecast, label="Forecast", color="orange", linestyle="--")
    plt.title(f"{asset_name} - ARIMA Forecast (Next 30 Days)")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.legend()
    plt.grid(True)
    os.makedirs("outputs/plots", exist_ok=True)
    plt.savefig(f"outputs/plots/{save_prefix}_forecast_plot.png")
    plt.show()
    print(f"\n {asset_name} forecast saved and plotted!\n")

if __name__ == "__main__":
    os.makedirs("data/forecast", exist_ok=True)

    arima_forecast("data/featured/spy_stock_featured.csv", "SPY", "spy")
    arima_forecast("data/featured/eurusd_fx_featured.csv", "EURUSD", "eurusd")
