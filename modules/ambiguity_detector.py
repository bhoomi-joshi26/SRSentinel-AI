"""
=========================================================
SRSentinel AI
Ambiguity Detection Module
=========================================================
"""
import re
class AmbiguityDetector:
    def __init__(self):
        self.ambiguous_words = {
            "fast": "Specify an exact response time.",
            "quick": "Specify measurable execution time.",
            "easy": "Describe measurable usability criteria.",
            "simple": "Define what 'simple' means.",
            "efficient": "Specify CPU, memory or execution limits.",
            "better": "State how much improvement is required.",
            "good": "Replace with measurable quality metrics.",
            "many": "Specify the exact number.",
            "large": "Specify the actual size.",
            "small": "Specify the exact value.",
            "soon": "Mention a definite deadline.",
            "appropriate": "State the required behavior clearly.",
            "proper": "Replace with measurable requirements.",
            "user-friendly": "Specify usability standards.",
            "user friendly": "Specify usability standards.",
            "secure": "Mention the security mechanism.",
            "robust": "Define fault tolerance criteria.",
            "flexible": "Specify configurable features.",
            "high": "Mention the required threshold.",
            "low": "Mention the acceptable limit."
        }

    # ----------------------------------------------------
    # Detect Ambiguous Words
    # ----------------------------------------------------

    def detect(self, text):
        if not text:
            return []
        found = []
        text = str(text).lower()
        for word in self.ambiguous_words:
            pattern = r"\b" + re.escape(word.lower()) + r"\b"
            if re.search(pattern, text, flags=re.IGNORECASE):
                found.append(word)
        return sorted(set(found))
    # ----------------------------------------------------
    # Count Ambiguous Words
    # ----------------------------------------------------

    def count(self, text):
        return len(self.detect(text))
    # ----------------------------------------------------
    # Check Whether Document Contains Ambiguity
    # ----------------------------------------------------

    def has_ambiguity(self, text):
        return self.count(text) > 0
    # ----------------------------------------------------
    # Highlight Ambiguous Words
    # ----------------------------------------------------

    def highlight(self, text):
        highlighted = text
        for word in self.ambiguous_words.keys():
            pattern = re.compile(
                r"\b" + re.escape(word) + r"\b",
                re.IGNORECASE
            )
            highlighted = pattern.sub(
                lambda match: f"🔴 {match.group(0).upper()}",
                highlighted
            )
        return highlighted
    # ----------------------------------------------------
    # Get Suggestions
    # ----------------------------------------------------

    def get_suggestions(self, text):
        detected = self.detect(text)
        suggestions = {}
        for word in detected:
            suggestions[word] = self.ambiguous_words[word]
        return suggestions
    # ----------------------------------------------------
    # Ambiguity Severity
    # ----------------------------------------------------

    def get_severity(self, text):
        total = self.count(text)
        if total == 0:
            return "None"
        elif total <= 2:
            return "Low"
        elif total <= 5:
            return "Medium"
        else:
            return "High"
    # ----------------------------------------------------
    # Ambiguity Score
    # ----------------------------------------------------

    def ambiguity_score(self, text):
        total = self.count(text)
        score = max(0, 100 - (total * 10))
        return score
    # ----------------------------------------------------
    # Generate Complete Report
    # ----------------------------------------------------

    def generate_report(self, text):
        detected = self.detect(text)
        report = {
            "ambiguous_words": detected,
            "count": self.count(text),
            "severity": self.get_severity(text),
            "ambiguity_score": self.ambiguity_score(text),
            "suggestions": self.get_suggestions(text),
            "highlighted_text": self.highlight(text)
        }
        return report
