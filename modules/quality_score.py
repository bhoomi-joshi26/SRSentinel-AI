"""
=========================================================
SRSentinel AI
Quality Score Module
=========================================================
"""
class QualityScore:
    def __init__(self):
        self.max_score = 100
    # --------------------------------------------------
    # Calculate Quality Score
    # --------------------------------------------------
    def calculate_score(
        self,
        total_requirements,
        ambiguous_words,
        functional,
        non_functional
    ):
        score = self.max_score
        # No requirements
        if total_requirements == 0:
            return 0
        # Ambiguity penalty
        score -= ambiguous_words * 5
        # Functional Requirement Coverage
        if functional == 0:
            score -= 20
        # Non-Functional Requirement Coverage
        if non_functional == 0:
            score -= 10
        # Too few requirements
        if total_requirements < 5:
            score -= 10
        # Keep score between 0 and 100
        score = max(0, min(score, 100))
        return round(score, 2)
    # --------------------------------------------------
    # Quality Grade
    # --------------------------------------------------
    def get_grade(self, score):
        if score >= 90:
            return "A+"
        elif score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "F"
    # --------------------------------------------------
    # Quality Status
    #---------------------------------------------------
    def get_status(self, score):
        if score >= 90:
            return "Excellent"
        elif score >= 80:
            return "Very Good"
        elif score >= 70:
            return "Good"
        elif score >= 60:
            return "Fair"
        elif score >= 40:
            return "Poor"
        return "Very Poor"
    # --------------------------------------------------
    # Quality Color
    # --------------------------------------------------
    def get_color(self, score):
        if score >= 90:
            return "#28A745"
        elif score >= 70:
            return "#FFC107"
        return "#DC3545"
    # --------------------------------------------------
    # Improvement Suggestions
    # --------------------------------------------------
    def get_suggestions(self, score):
        suggestions = []
        if score >= 90:
            suggestions.append(
                "Excellent SRS document. No major improvements required."
            )
        if score < 90:
            suggestions.append(
                "Reduce ambiguous words such as fast, easy, better and efficient."
            )
        if score < 80:
            suggestions.append(
                "Write measurable and testable requirements."
            )
        if score < 70:
            suggestions.append(
                "Include more Functional and Non-Functional requirements."
            )
        if score < 60:
            suggestions.append(
                "Review the SRS document before implementation."
            )
        return suggestions
    # --------------------------------------------------
    # Quality Percentage
    # --------------------------------------------------
    def get_percentage(self, score):
        return round((score / self.max_score) * 100, 2)
    # --------------------------------------------------
    # Complete Quality Report
    # --------------------------------------------------
    def generate_report(
        self,
        total_requirements,
        ambiguous_words,
        functional,
        non_functional
    ):
        score = self.calculate_score(
            total_requirements,
            ambiguous_words,
            functional,
            non_functional
        )
        return {
            "quality_score": score,
            "percentage": self.get_percentage(score),
            "grade": self.get_grade(score),
            "status": self.get_status(score),
            "color": self.get_color(score),
            "suggestions": self.get_suggestions(score)
        }