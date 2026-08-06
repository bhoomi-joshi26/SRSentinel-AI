"""
=========================================================
SRSentinel AI
Utility Functions
=========================================================
"""

import os


def file_extension(filename):
    """Return file extension."""
    return os.path.splitext(filename)[1].lower()


def is_pdf(filename):
    return file_extension(filename) == ".pdf"


def is_docx(filename):
    return file_extension(filename) == ".docx"


def format_percentage(value):
    return f"{round(value, 2)}%"


def safe_text(text):
    """Return empty string if None."""
    return "" if text is None else str(text)