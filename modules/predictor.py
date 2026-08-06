"""
=========================================================
SRSentinel AI
Prediction Module
=========================================================
"""
import os
import joblib
import numpy as np


class Predictor:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(
            base_dir,
            "models",
            "model.pkl"
        )
        vectorizer_path = os.path.join(
            base_dir,
            "models",
            "vectorizer.pkl"
        )
        # ----------------------------------------------
        # Load Model
        # ----------------------------------------------
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                "model.pkl not found. Please run train_model.py first."
            )
        if not os.path.exists(vectorizer_path):
            raise FileNotFoundError(
                "vectorizer.pkl not found. Please run train_model.py first."
            )
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
        # ----------------------------------------------------
        # Transform Text
        # ----------------------------------------------------

    def transform(self, cleaned_text):
        return self.vectorizer.transform(
            [cleaned_text]
        )
    # ----------------------------------------------------
    # Predict Requirement Quality
    # ---------------------------------------------------

    def predict(self, cleaned_text):
        vector = self.transform(cleaned_text)
        prediction = self.model.predict(vector)[0]
        probability = self.model.predict_proba(vector)[0]
        confidence = round(
            np.max(probability) * 100,
            2
        )
        return prediction, confidence
    # ----------------------------------------------------
    # Get Prediction Probabilities
    # ----------------------------------------------------

    def prediction_probabilities(self, cleaned_text):
        vector = self.transform(cleaned_text)
        probability = self.model.predict_proba(vector)[0]
        classes = self.model.classes_
        return {
            str(classes[0]): round(probability[0] * 100, 2),
            str(classes[1]): round(probability[1] * 100, 2)
        }
    # ----------------------------------------------------
    # Get Quality Label
    # ----------------------------------------------------

    def get_quality_label(self, prediction):
        prediction = str(prediction).strip().lower()
        if prediction in ["high", "1"]:
            return "High Quality"
        elif prediction in ["low", "0"]:
            return "Low Quality"
        else:
            return "Unknown"
    # ----------------------------------------------------
    # Get Status Color
    # ----------------------------------------------------

    def get_status_color(self, confidence):
        if confidence >= 90:
            return "green"
        elif confidence >= 75:
            return "orange"
        else:
            return "red"
    # ----------------------------------------------------
    # Confidence Level
    # ----------------------------------------------------

    def confidence_level(self, confidence):
        if confidence >= 95:
            return "Very High"
        elif confidence >= 85:
            return "High"
        elif confidence >= 70:
            return "Moderate"
        else:
            return "Low"
    # ----------------------------------------------------
    # Prediction Explanation
    # ----------------------------------------------------

    def prediction_explanation(self, prediction):
        prediction = str(prediction).strip().lower()
        if prediction == "high" or prediction == "1":
            return (
                "The uploaded SRS document follows good "
                "requirement writing practices. Most "
                "requirements appear clear, measurable, "
                "and less ambiguous."
            )
        elif prediction == "low" or prediction == "0":
            return (
                "The uploaded SRS document contains poor "
                "quality requirements or ambiguous "
                "statements. Requirement improvement "
                "is recommended."
            )

        else:
            return "Prediction unavailable."
    # ----------------------------------------------------
    # Prediction Summary
    # ----------------------------------------------------

    def prediction_summary(self, cleaned_text):
        prediction, confidence = self.predict(cleaned_text)
        probabilities = self.prediction_probabilities(cleaned_text)
        quality = self.get_quality_label(prediction)
        color = self.get_status_color(confidence)
        level = self.confidence_level(confidence)
        explanation = self.prediction_explanation(prediction)
        return {
            "prediction": prediction,
            "quality": quality,
            "confidence": confidence,
            "confidence_level": level,
            "status_color": color,
            "high_probability": probabilities["High"],
            "low_probability": probabilities["Low"],
            "explanation": explanation
        }
    # ----------------------------------------------------
    # Complete Prediction Report
    # ----------------------------------------------------

    def generate_prediction_report(self, cleaned_text):
        summary = self.prediction_summary(cleaned_text)
        report = {
            "prediction": summary["prediction"],
            "quality": summary["quality"],
            "confidence": summary["confidence"],
            "confidence_level": summary["confidence_level"],
            "status_color": summary["status_color"],
            "high_probability": summary["high_probability"],
            "low_probability": summary["low_probability"],
            "explanation": summary["explanation"]
        }
        return report
