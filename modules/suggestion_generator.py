"""
=========================================================
SRSentinel AI
Suggestion Generator Module
=========================================================
"""

class SuggestionGenerator:

    def __init__(self):

        self.ambiguity_suggestions = {

            "fast":
                "Specify an exact response time (e.g., within 2 seconds).",

            "easy":
                "Define measurable usability requirements.",

            "better":
                "State measurable improvement criteria.",

            "efficient":
                "Specify CPU, memory or execution constraints.",

            "many":
                "Specify the exact number instead of using 'many'.",

            "large":
                "Mention the exact size or capacity.",

            "small":
                "Specify the actual value.",

            "good":
                "Replace with measurable quality attributes.",

            "quick":
                "Mention an exact execution time.",

            "secure":
                "Specify encryption or authentication mechanisms.",

            "simple":
                "Describe measurable usability goals.",

            "robust":
                "Mention fault tolerance requirements.",

            "flexible":
                "Specify configurable functions.",

            "appropriate":
                "Replace with precise system behaviour.",

            "proper":
                "Use measurable and testable statements."

        }
            # --------------------------------------------------
    # Suggestions for Ambiguous Words
    # --------------------------------------------------

    def ambiguity_recommendations(self, ambiguous_words):

        recommendations = []

        for word in ambiguous_words:

            if word in self.ambiguity_suggestions:

                recommendations.append(

                    self.ambiguity_suggestions[word]

                )

        return recommendations
        # --------------------------------------------------
    # Functional Requirement Suggestions
    # --------------------------------------------------

    def functional_recommendations(self, functional_count):

        suggestions = []

        if functional_count == 0:

            suggestions.append(

                "Add Functional Requirements using statements such as 'The system shall...'"

            )

        elif functional_count < 5:

            suggestions.append(

                "Increase the number of Functional Requirements."

            )

        else:

            suggestions.append(

                "Functional Requirement coverage is satisfactory."

            )

        return suggestions
        # --------------------------------------------------
    # Non Functional Requirement Suggestions
    # --------------------------------------------------

    def non_functional_recommendations(self, nfr_count):

        suggestions = []

        if nfr_count == 0:

            suggestions.append(

                "Include Non-Functional Requirements such as performance, security and reliability."

            )

        elif nfr_count < 3:

            suggestions.append(

                "Consider adding more Non-Functional Requirements."

            )

        else:

            suggestions.append(

                "Non-Functional Requirement coverage is satisfactory."

            )

        return suggestions
        # --------------------------------------------------
    # Overall Improvement Checklist
    # --------------------------------------------------

    def improvement_checklist(self, quality_score):

        checklist = []

        if quality_score >= 90:

            checklist.append("✔ Requirements are clear and well-defined.")
            checklist.append("✔ Maintain the current documentation quality.")

        else:

            checklist.append("✔ Remove ambiguous words.")
            checklist.append("✔ Write measurable requirements.")
            checklist.append("✔ Include both Functional and Non-Functional Requirements.")
            checklist.append("✔ Use 'The system shall...' wherever applicable.")
            checklist.append("✔ Review the document before implementation.")

        return checklist

    # --------------------------------------------------
    # Best Practices
    # --------------------------------------------------

    def best_practices(self):

        return [

            "Use clear and concise language.",

            "Avoid vague and subjective words.",

            "Write measurable and testable requirements.",

            "Separate Functional and Non-Functional Requirements.",

            "Ensure every requirement is complete and consistent.",

            "Specify performance, security and reliability constraints.",

            "Review the SRS document regularly."

        ]

    # --------------------------------------------------
    # Generate Complete Suggestion Report
    # --------------------------------------------------

    def generate_report(

        self,

        ambiguous_words,

        functional_count,

        non_functional_count,

        quality_score

    ):

        report = {

            "ambiguity_suggestions":

                self.ambiguity_recommendations(

                    ambiguous_words

                ),

            "functional_suggestions":

                self.functional_recommendations(

                    functional_count

                ),

            "non_functional_suggestions":

                self.non_functional_recommendations(

                    non_functional_count

                ),

            "improvement_checklist":

                self.improvement_checklist(

                    quality_score

                ),

            "best_practices":

                self.best_practices()

        }

        return report


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    generator = SuggestionGenerator()

    report = generator.generate_report(

        ambiguous_words=["fast", "easy", "better"],

        functional_count=3,

        non_functional_count=2,

        quality_score=72

    )

    print("\n" + "=" * 60)
    print("SUGGESTION REPORT")
    print("=" * 60)

    print("\nAmbiguity Suggestions")

    for item in report["ambiguity_suggestions"]:

        print("-", item)

    print("\nFunctional Suggestions")

    for item in report["functional_suggestions"]:

        print("-", item)

    print("\nNon-Functional Suggestions")

    for item in report["non_functional_suggestions"]:

        print("-", item)

    print("\nImprovement Checklist")

    for item in report["improvement_checklist"]:

        print("-", item)

    print("\nBest Practices")

    for item in report["best_practices"]:

        print("-", item)

    print("\n" + "=" * 60)
    print("Suggestion Generator Executed Successfully")
    print("=" * 60)