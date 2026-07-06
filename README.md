# Nexus Bank — Financial Analytics Capstone

A multi-domain financial analytics pipeline covering **credit card fraud detection** and **stock market forecasting**. Built as a capstone project simulating real-world data engineering and ML workflows in a banking/fintech context.

---

## Project Overview

| Domain | Task | Approach |
|---|---|---|
| Fraud Detection | Binary classification on credit card transactions | Logistic Regression, ROC-AUC |
| Market Forecasting | 30-day price forecast for SPY & EUR/USD | ARIMA(5,1,0) |
| Technical Analysis | Feature engineering on OHLCV data | SMA, EMA, RSI, Bollinger Bands |

---

## Repository Structure

```
nexus-bank-capstone/
├── scripts/
│   ├── fetch.py                          # yfinance data ingestion (SPY, EUR/USD)
│   ├── feature_engineering.py            # Technical indicators (SMA, EMA, RSI, Bollinger Bands)
│   ├── model_fraud_detection.py          # Logistic Regression fraud classifier
│   ├── arima_forecast.py                 # ARIMA 30-day price forecasting
│   ├── visualizations.py                 # ROC curve, confusion matrix plots
│   ├── featured_visualization.py         # Technical indicator plots
│   ├── Final_Cleaned_Data_Credit_Card_Fraud_.ipynb
│   ├── Final_Data_Cleaning_Eurusd_Fx.ipynb
│   └── Final_Data_Cleaning_Spy_Stock.ipynb
├── notebooks/
│   └── 01_data_summary.ipynb             # Exploratory data analysis
├── models/
│   └── logreg_fraud_model.pkl            # Saved fraud detection model
├── logs/                                  # Auto-generated data fetch logs
├── data/                                  # Raw, cleaned, featured, forecast CSVs
├── outputs/plots/                         # Generated visualisation images
├── reports/
└── requirements.txt
```

---

## Pipeline

```
Data Ingestion          Feature Engineering       Modelling & Forecasting
─────────────          ───────────────────       ───────────────────────
yfinance (SPY,    →    SMA-14, EMA-14,      →    Fraud: Logistic Regression
EUR/USD) + Kaggle      RSI-14, Bollinger          Stock: ARIMA(5,1,0)
credit card data       Bands, Volatility,          30-day forecast
                       Price Change (%)
                            │
                            ▼
                       Visualisation
                       ─────────────
                       ROC curve, Confusion matrix,
                       Bollinger Band plots,
                       ARIMA forecast charts
```

---

## Module Breakdown

### `fetch.py` — Data Ingestion
Downloads historical OHLCV data for SPY and EUR/USD from Yahoo Finance using `yfinance`. Saves raw CSVs to `data/raw/` and writes timestamped logs to `logs/`.

```bash
python scripts/fetch.py
```

### `feature_engineering.py` — Technical Indicators
Computes financial features on cleaned OHLCV data:

| Feature | Description |
|---|---|
| `SMA_14` | Simple Moving Average (14-day window) |
| `EMA_14` | Exponential Moving Average (14-day) |
| `RSI_14` | Relative Strength Index |
| `Bollinger_High/Mid/Low` | 20-day Bollinger Bands |
| `Volatility` | Rolling standard deviation (14-day) |
| `Price_Change` | Daily percentage change |

```bash
python scripts/feature_engineering.py
```

### `model_fraud_detection.py` — Fraud Classifier
Trains a Logistic Regression model on the Kaggle Credit Card Fraud dataset. Evaluates with classification report, confusion matrix, and ROC-AUC score. Saves the trained model to `models/logreg_fraud_model.pkl`.

```bash
python scripts/model_fraud_detection.py
```

**Model results:**
```
ROC-AUC Score: ~0.97
Dataset: Kaggle Credit Card Fraud (284,807 transactions, 492 fraud cases)
Class imbalance: 0.172% fraud
```

### `arima_forecast.py` — Time Series Forecasting
Fits an ARIMA(5,1,0) model on the last available closing prices and forecasts the next **30 days** for both SPY and EUR/USD. Saves forecast CSVs and plots to `outputs/plots/`.

```bash
python scripts/arima_forecast.py
```

### `visualizations.py` — Model Evaluation Plots
Generates ROC curve and confusion matrix heatmap for the fraud detection model.

```bash
python scripts/visualizations.py
```

---

## Setup

```bash
git clone https://github.com/saiswaroopkakarla/nexus-bank-capstone.git
cd nexus-bank-capstone
pip install -r requirements.txt
```

### Run full pipeline

```bash
# 1. Fetch raw data
python scripts/fetch.py

# 2. Clean data (use provided notebooks or manually place CSVs in data/cleaned/)

# 3. Engineer features
python scripts/feature_engineering.py

# 4. Train fraud model
python scripts/model_fraud_detection.py

# 5. Forecast prices
python scripts/arima_forecast.py

# 6. Generate visualisations
python scripts/visualizations.py
python scripts/featured_visualization.py
```

---

## Tech Stack

| Library | Purpose |
|---|---|
| `yfinance` | Stock & forex data ingestion |
| `pandas`, `numpy` | Data manipulation |
| `scikit-learn` | Logistic Regression, metrics |
| `statsmodels` | ARIMA forecasting |
| `matplotlib`, `seaborn` | Visualisation |
| `joblib` | Model serialisation |

---

## TODOs

- [ ] Data cleaning notebooks should be converted to standalone scripts for full pipeline automation
- [ ] `visualizations.py` `__main__` block is incomplete — plots need to be wired up
- [ ] `data/` folder uses `.gitkeep` — raw/cleaned CSVs need to be downloaded locally (see `fetch.py`)
- [ ] Consider adding SMOTE or class-weight balancing for improved fraud recall

---

## Author

**Kakarla Sai Swaroop**  
M25DE1023 — IIT Jodhpur, M.Tech Data Engineering
