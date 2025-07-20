import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import os

# Load cleaned dataset
df = pd.read_csv("data/cleaned/credit_card_fraud_cleaned.csv")

# Separate features and target
X = df.drop("Class", axis=1)
y = df["Class"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

print("\n --Classification Report:\n")
print(classification_report(y_test, y_pred))

print("\n --Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

roc_auc = roc_auc_score(y_test, y_proba)
print(f"\n --ROC-AUC Score: {roc_auc:.4f}")

# Save model if needed later
import joblib
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/logreg_fraud_model.pkl")
print("\n --Model saved to models/logreg_fraud_model.pkl")
