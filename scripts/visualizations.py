import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib
from sklearn.metrics import roc_curve, auc, confusion_matrix

def plot_forecast(file_path, title, save_name):
    df = pd.read_csv(file_path)
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Forecast_Close'], label="Forecast", color="orange")
    plt.title(f"{title} - Forecasted Close Price")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"outputs/plots/{save_name}_only_forecast.png")
    plt.close()

def plot_roc_curve():
    df = pd.read_csv("data/cleaned/credit_card_fraud_cleaned.csv")
    X = df.drop("Class", axis=1)
    y = df["Class"]

    model = joblib.load("models/logreg_fraud_model.pkl")
    y_proba = model.predict_proba(X)[:, 1]

    fpr, tpr, _ = roc_curve(y, y_proba)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(8,6))
    plt.plot(fpr, tpr, label=f"ROC curve (AUC = {roc_auc:.4f})")
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
    plt.title("ROC Curve - Credit Card Fraud Detection")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("outputs/plots/fraud_roc_curve.png")
    plt.close()

def plot_conf_matrix():
    df = pd.read_csv("data/cleaned/credit_card_fraud_cleaned.csv")
    X = df.drop("Class", axis=1)
    y = df["Class"]

    model = joblib.load("models/logreg_fraud_model.pkl")
    y_pred = model.predict(X)
    cm = confusion_matrix(y, y_pred)

    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix - Fraud Detection")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig("outputs/plots/fraud_conf_matrix.png")
    plt.close()

if __name__ == "__main__":
    plot_forecast("data/forecast/spy_forecast.csv", "SPY", "spy")
    plot_forecast("data/forecast/eurusd_forecast.csv", "EURUSD", "eurusd")
    plot_roc_curve()
    plot_conf_matrix()
    print("\n All visualizations saved in outputs/plots/")
