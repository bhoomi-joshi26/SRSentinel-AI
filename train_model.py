"""pd
=========================================================
SRSentinel AI
Machine Learning Model Training
=========================================================
"""
import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
# =========================================================
# Paths
# =========================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "srs_dataset.csv"
)
MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)
MODEL_PATH = os.path.join(
    MODEL_DIR,
    "model.pkl"
)
VECTORIZER_PATH = os.path.join(
    MODEL_DIR,
    "vectorizer.pkl"
)
os.makedirs(
    MODEL_DIR,
    exist_ok=True
)
# =========================================================
# Load Dataset
# =========================================================
print("=" * 60)
print("Loading Dataset...")
# Check if dataset file exists
if not os.path.exists(DATASET_PATH):
    raise FileNotFoundError(
        f"Dataset not found:\n{DATASET_PATH}"
    )
# Load dataset
dataset = pd.read_csv(DATASET_PATH)
# Validate required columns
required_columns = {"requirement", "label"}
if not required_columns.issubset(dataset.columns):
    raise ValueError(
        "Dataset must contain 'requirement' and 'label' columns."
    )
print(dataset.head())
print()
print("Total Samples :", len(dataset))
# =========================================================
# Dataset Cleaning
# =========================================================
dataset = dataset.dropna()
dataset = dataset.drop_duplicates(
    subset="requirement"
)
dataset = dataset.reset_index(drop=True)
print()
print("Samples After Cleaning :", len(dataset))
# =========================================================
# Input and Output
# =========================================================
X = dataset["requirement"].astype(str)
y = dataset["label"]
# =========================================================
# Train-Test Split
# =========================================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
# =========================================================
# TF-IDF Vectorization
# =========================================================
print("\nCreating TF-IDF Features...")
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=5000,
    ngram_range=(1, 2)
)
X_train_vector = vectorizer.fit_transform(X_train)
X_test_vector = vectorizer.transform(X_test)
# =========================================================
# Train Random Forest Model
# =========================================================
print("Training Random Forest Model...")
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train_vector, y_train)
# =========================================================
# Model Evaluation
# =========================================================
print("\nEvaluating Model...")
y_pred = model.predict(X_test_vector)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy : {accuracy * 100:.2f}%")
print("\nClassification Report\n")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, y_pred))
# =========================================================
# Save Model
# =========================================================
joblib.dump(
    model,
    MODEL_PATH
)
joblib.dump(
    vectorizer,
    VECTORIZER_PATH
)
print("\nModel Saved Successfully")
print(f"Model saved to:\n{MODEL_PATH}")
print("\nVectorizer Saved Successfully")
print(f"Vectorizer saved to:\n{VECTORIZER_PATH}")
print("\n" + "=" * 60)
print("SRSentinel AI Training Completed Successfully")
print("=" * 60)