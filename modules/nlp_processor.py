"""
=========================================================
SRSentinel AI
Natural Language Processing Module
=========================================================
"""
import re
import string
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# --------------------------------------------------------
# Download NLTK Resources
# --------------------------------------------------------
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")
try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")

try:
    nltk.data.find("corpora/omw-1.4")
except LookupError:
    nltk.download("omw-1.4")
class NLPProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()
        # Ambiguous words commonly found in SRS documents
        self.ambiguous_words = [
            # Time
            "fast",
            "quick",
            "quickly",
            "soon",
            "immediately",
            "rapidly",
            "timely",
            # Quality
            "good",
            "better",
            "best",
            "efficient",
            "effective",
            "appropriate",
            "proper",
            "suitable",
            "optimal",
            "robust",
            # User Experience
            "easy",
            "simple",
            "user friendly",
            "user-friendly",
            "convenient",
            "intuitive",
            "flexible",
            # Quantity
            "many",
            "few",
            "several",
            "large",
            "small",
            "high",
            "low",
            "enough",
            "adequate",
            "maximum",
            "minimum",
            # Performance
            "fast response",
            "high performance",
            "low latency",
            "quick response",
            # Security
            "secure",
            "safe",
            "protected",
            # Frequency
            "often",
            "frequently",
            "regularly",
            "normally",
            "usually",
            # Requirement uncertainty
            "should",
            "may",
            "might",
            "could",
            "if required",
            "when needed",
            # General vague words
            "etc",
            "and so on",
            "various",
            "multiple",
            "similar",
            "related"
        ]
    # ----------------------------------------------------
    # Clean Text
    # ----------------------------------------------------
    def clean_text(self, text):
        if not isinstance(text, str):
            text = str(text)
        text = text.lower()
        # Remove numbers
        text = re.sub(r"\d+", "", text)
        # Keep alphabets, spaces and hyphen
        text = re.sub(r"[^a-zA-Z\s\-]", "", text)
        # Remove extra spaces
        text = " ".join(text.split())
        return text
    # ----------------------------------------------------
    # Remove Punctuation
    # ----------------------------------------------------
    def remove_punctuation(self, text):
        return text.translate(
            str.maketrans("", "", string.punctuation)
        )
    # ----------------------------------------------------
    # Remove Numbers
    # ----------------------------------------------------
    def remove_numbers(self, text):
        return re.sub(r"\d+", "", text)
    # ----------------------------------------------------
    # Remove Extra Spaces
    # ----------------------------------------------------
    def remove_extra_spaces(self, text):
        return " ".join(text.split())
    # ----------------------------------------------------
    # Sentence Tokenization
    # ----------------------------------------------------
    def sentence_tokenize(self, text):
        return sent_tokenize(text)
    # ----------------------------------------------------
    # Word Tokenization
    # ----------------------------------------------------
    def word_tokenize_text(self, text):
        return word_tokenize(text)
    # ----------------------------------------------------
    # Remove Stopwords
    # ----------------------------------------------------
    def remove_stopwords(self, words):
        return [
            word
            for word in words
            if word not in self.stop_words
        ]
    # ----------------------------------------------------
    # Lemmatization
    # ----------------------------------------------------
    def lemmatize_words(self, words):
        return [
            self.lemmatizer.lemmatize(word)
            for word in words
        ]
    # ----------------------------------------------------
    # Complete Text Preprocessing
    # ----------------------------------------------------
    def preprocess(self, text):
        text = self.clean_text(text)
        words = self.word_tokenize_text(text)
        words = self.remove_stopwords(words)
        words = self.lemmatize_words(words)
        return " ".join(words)
    # ----------------------------------------------------
    # Functional Requirement Detection
    # ----------------------------------------------------
    def detect_functional_requirements(self, sentences):
        functional_keywords = [
            "shall",
            "must",
            "allow",
            "provide",
            "create",
            "update",
            "delete",
            "insert",
            "modify",
            "generate",
            "display",
            "calculate",
            "login",
            "logout",
            "register",
            "authenticate",
            "authorize",
            "upload",
            "download",
            "search",
            "print",
            "send",
            "receive",
            "store",
            "retrieve"
        ]
        functional = []
        for sentence in sentences:
            sentence_lower = sentence.lower()
            if any(keyword in sentence_lower for keyword in functional_keywords):
                functional.append(sentence)
        return functional
    # ----------------------------------------------------
    # Non-Functional Requirement Detection
    # ----------------------------------------------------
    def detect_non_functional_requirements(self, sentences):
        nfr_keywords = [
            "performance",
            "security",
            "reliability",
            "availability",
            "maintainability",
            "usability",
            "scalability",
            "response time",
            "speed",
            "accuracy",
            "privacy",
            "encryption",
            "authentication",
            "authorization",
            "backup",
            "recovery",
            "compatibility",
            "portability",
            "efficiency"
        ]
        non_functional = []
        for sentence in sentences:
            sentence_lower = sentence.lower()
            if any(keyword in sentence_lower for keyword in nfr_keywords):
                non_functional.append(sentence)
        return non_functional
    # ----------------------------------------------------
    # Ambiguous Word Detection
    # ----------------------------------------------------
    def detect_ambiguous_words(self, text):
        found_words = []
        text_lower = text.lower()
        for word in self.ambiguous_words:
            if word in text_lower:
                found_words.append(word)
        return sorted(set(found_words))
    # ----------------------------------------------------
    # Requirement Statistics
    # ----------------------------------------------------
    def get_statistics(self, sentences):
        functional = self.detect_functional_requirements(sentences)
        non_functional = self.detect_non_functional_requirements(sentences)
        return {
            "total_requirements": len(sentences),
            "functional_requirements": len(functional),
            "non_functional_requirements": len(non_functional),
            "ambiguous_requirements": len(
                [
                    sentence
                    for sentence in sentences
                    if self.detect_ambiguous_words(sentence)
                ]
            )
        }
    # ----------------------------------------------------
    # Highlight Ambiguous Words
    # ----------------------------------------------------
    def highlight_ambiguous_words(self, text):
        highlighted = text
        for word in self.ambiguous_words:
            pattern = re.compile(
                r"\b" + re.escape(word) + r"\b",
                re.IGNORECASE
            )
            highlighted = pattern.sub(
                f"🔴 **{word.upper()}**",
                highlighted
            )
        return highlighted
    # ----------------------------------------------------
    # Complete NLP Analysis
    # ----------------------------------------------------
    def analyze_document(self, text):
        sentences = self.sentence_tokenize(text)
        cleaned_text = self.preprocess(text)
        functional = self.detect_functional_requirements(sentences)
        non_functional = self.detect_non_functional_requirements(sentences)
        ambiguous = self.detect_ambiguous_words(text)
        statistics = self.get_statistics(sentences)
        highlighted = self.highlight_ambiguous_words(text)
        return {
            "original_text": text,
            "clean_text": cleaned_text,
            "sentences": sentences,
            "functional_requirements": functional,
            "non_functional_requirements": non_functional,
            "ambiguous_words": ambiguous,
            "highlighted_text": highlighted,
            "statistics": statistics
        }
        
        