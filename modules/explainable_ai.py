"""
=========================================================
SRSentinel AI
Explainable Artificial Intelligence Module
=========================================================
"""


class ExplainableAI:
    def __init__(self):
        self.positive_rules = {
            "functional_requirements":
                "Functional requirements are properly defined.",
            "non_functional_requirements":
                "Non-Functional requirements are present.",
            "low_ambiguity":
                "Very few ambiguous words detected.",
            "high_quality":
                "Machine Learning model predicts High Quality."
        }
        self.negative_rules = {
            "ambiguity":
                "Ambiguous words reduce requirement clarity.",
            "missing_functional":
                "Functional requirements are insufficient.",
            "missing_nonfunctional":
                "Non-Functional requirements are insufficient.",
            "low_quality":
                "Machine Learning model predicts Low Quality."
        }
    # --------------------------------------------------
    # Positive Indicators
    # --------------------------------------------------

    def positive_indicators(
        self,
        quality,
        ambiguity_count,
        functional,
        non_functional
    ):
        positives = []
        if str(quality).lower().startswith("high"):
            positives.append(
                self.positive_rules["high_quality"]
            )
        if ambiguity_count <= 2:
            positives.append(
                self.positive_rules["low_ambiguity"]
            )
        if functional > 0:
            positives.append(
                self.positive_rules["functional_requirements"]
            )
        if non_functional > 0:
            positives.append(
                self.positive_rules["non_functional_requirements"]
            )
        return positives
    # --------------------------------------------------
    # Negative Indicators
    # --------------------------------------------------

    def negative_indicators(
        self,
        quality,
        ambiguity_count,
        functional,
        non_functional
    ):
        negatives = []
        if str(quality).lower().startswith("low"):
            negatives.append(
                self.negative_rules["low_quality"]
            )
        if ambiguity_count > 2:
            negatives.append(
                self.negative_rules["ambiguity"]
            )
        if functional == 0:
            negatives.append(
                self.negative_rules["missing_functional"]
            )
        if non_functional == 0:
            negatives.append(
                self.negative_rules["missing_nonfunctional"]
            )
        return negatives
    # --------------------------------------------------
    # Feature Importance Summary
    # --------------------------------------------------

    def feature_importance(
        self,
        ambiguity_count,
        quality_score,
        functional,
        non_functional
    ):
        features = {
            "Requirement Quality Score": quality_score,
            "Requirement Clarity": round(max(0, 100 - ambiguity_count * 10), 2),
            "Ambiguous Words": ambiguity_count,
            "Functional Requirements": functional,
            "Non-Functional Requirements": non_functional
        }
        return features
    # --------------------------------------------------
    # Human Readable Explanation
    # --------------------------------------------------

    def generate_explanation(
        self,
        quality,
        quality_score,
        ambiguity_count,
        functional,
        non_functional
    ):
        explanation = f"""
The uploaded Software Requirement Specification (SRS)
document was analyzed using Natural Language Processing
(NLP) and a Machine Learning model to evaluate the quality,
clarity and completeness of software requirements.

Prediction : {quality}

Quality Score : {quality_score}/100

Functional Requirements : {functional}

Non Functional Requirements : {non_functional}

Ambiguous Words : {ambiguity_count}

The prediction is mainly influenced by requirement
coverage, requirement clarity, and the number of
ambiguous words detected in the document.

"""
        return explanation.strip()
    # --------------------------------------------------
    # Explainable AI Report
    # --------------------------------------------------

    def generate_report(
            self,
            quality,
            quality_score,
            ambiguity_count,
            functional,
            non_functional
        ):


        positive_indicators = []

        negative_indicators = []

        feature_importance = {}



        # Positive Analysis

        if quality_score >= 75:

            positive_indicators.append(
                "Overall SRS quality score is high."
            )

        else:

            negative_indicators.append(
                "SRS quality score needs improvement."
            )



        if functional > 0:

            positive_indicators.append(
                "Functional requirements are clearly identified."
            )



        if non_functional > 0:

            positive_indicators.append(
                "Non-functional requirements are present."
            )



        # Ambiguity Analysis

        if ambiguity_count == 0:

            positive_indicators.append(
                "No ambiguous terms detected."
            )

        else:

            negative_indicators.append(
                f"{ambiguity_count} ambiguous terms detected."
            )



        feature_importance = {

            "Quality Score": quality_score,

            "Ambiguity Count": ambiguity_count,

            "Functional Requirements": functional,

            "Non Functional Requirements": non_functional

        }



        explanation = (

            f"The SRS is predicted as {quality}. "

            f"The quality score is {quality_score}/100. "

            f"The document contains {functional} functional "

            f"and {non_functional} non-functional requirements."

        )



        return {

            "positive_indicators": positive_indicators,

            "negative_indicators": negative_indicators,

            "feature_importance": feature_importance,

            "explanation": explanation

        }
