"""
=========================================================
SRSentinel AI
Feature Extractor Module
=========================================================
"""
import joblib
import os
class FeatureExtractor:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        vectorizer_path = os.path.join(
            base_dir,
            "models",
            "vectorizer.pkl"
        )
        if not os.path.exists(vectorizer_path):
                raise FileNotFoundError(
                        f"Vectorizer not found:\n{vectorizer_path}"
    )
        self.vectorizer = joblib.load(vectorizer_path)
    # ----------------------------------------------------
    # Extract TF-IDF Features
    # ----------------------------------------------------
    def extract_features(self, text):
        return self.vectorizer.transform([text])
    # ----------------------------------------------------
    # Get Feature Names
    # ----------------------------------------------------
    def get_feature_names(self):
        return self.vectorizer.get_feature_names_out()
    # ----------------------------------------------------
    # Number of Features
    # ----------------------------------------------------
    def feature_count(self):
        return len(self.vectorizer.get_feature_names_out())