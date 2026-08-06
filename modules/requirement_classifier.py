"""
=========================================================
SRSentinel AI
Requirement Classification Module
=========================================================
"""

import re


class RequirementClassifier:

    def __init__(self):

        self.functional_keywords = [

            "shall",
            "allow",
            "login",
            "logout",
            "register",
            "upload",
            "download",
            "insert",
            "update",
            "delete",
            "generate",
            "display",
            "search",
            "authenticate",
            "calculate",
            "verify",
            "send",
            "receive",
            "print",
            "store",
            "create",
            "modify",
            "view",
            "export",
            "import",
            "retrieve"

        ]


        self.non_functional_keywords = [

            "performance",
            "response time",
            "processing time",
            "security",
            "authentication",
            "authorization",
            "encryption",
            "confidentiality",
            "privacy",
            "reliability",
            "availability",
            "backup",
            "recovery",
            "usability",
            "user friendly",
            "maintainability",
            "scalability",
            "compatibility",
            "portability",
            "accuracy",
            "compliance",
            "standard",
            "regulation",
            "timeout",
            "response"

        ]


    # --------------------------------------------------
    # Split Requirements
    # --------------------------------------------------

    def split_requirements(self, text):

        requirements = []

        lines = re.split(r"\n+|\.\s+", text)


        for line in lines:

            line = line.strip()

            if line:

                requirements.append(line)


        return requirements



    # --------------------------------------------------
    # Classify Single Requirement
    # --------------------------------------------------

    def classify_requirement(self, requirement):

        sentence = requirement.lower()


        functional_score = 0

        non_functional_score = 0


        for keyword in self.functional_keywords:

            if keyword in sentence:

                functional_score += 1



        for keyword in self.non_functional_keywords:

            if keyword in sentence:

                non_functional_score += 1



        if functional_score > non_functional_score:

            return "Functional"



        elif non_functional_score > functional_score:

            return "Non Functional"



        elif functional_score > 0:

            return "Functional"



        return "Other"



    # --------------------------------------------------
    # Classify Complete Document
    # --------------------------------------------------

    def classify_document(self, text):

        requirements = self.split_requirements(text)


        functional = []

        non_functional = []

        others = []


        for requirement in requirements:


            result = self.classify_requirement(requirement)



            if result == "Functional":

                functional.append(requirement)



            elif result == "Non Functional":

                non_functional.append(requirement)



            else:

                others.append(requirement)



        return {

            "functional": functional,

            "non_functional": non_functional,

            "others": others

        }



    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def get_statistics(self, text):

        result = self.classify_document(text)


        functional_count = len(result["functional"])

        non_functional_count = len(result["non_functional"])

        other_count = len(result["others"])


        total = (
            functional_count
            +
            non_functional_count
            +
            other_count
        )


        return {

            "total": total,

            "functional": functional_count,

            "non_functional": non_functional_count,

            "others": other_count

        }



    # --------------------------------------------------
    # Percentage
    # --------------------------------------------------

    def get_percentages(self, text):

        stats = self.get_statistics(text)

        total = stats["total"]


        if total == 0:

            return {

                "functional_percentage":0,

                "non_functional_percentage":0,

                "others_percentage":0

            }


        return {

            "functional_percentage":
                round((stats["functional"]/total)*100,2),


            "non_functional_percentage":
                round((stats["non_functional"]/total)*100,2),


            "others_percentage":
                round((stats["others"]/total)*100,2)

        }



    # --------------------------------------------------
    # Complete Classification Report
    # --------------------------------------------------

    def generate_report(self, text):


        result = self.classify_document(text)


        statistics = self.get_statistics(text)



        return {


            "functional_requirements":
                result["functional"],


            "non_functional_requirements":
                result["non_functional"],


            "other_requirements":
                result["others"],


            "statistics":
                statistics

        }