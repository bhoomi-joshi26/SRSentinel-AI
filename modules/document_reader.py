"""
=========================================================
SRSentinel AI
Document Reader Module
Supports:
• PDF
• DOCX
• TXT
=========================================================
"""

import os

from pypdf import PdfReader

from docx import Document


class DocumentReader:

    def __init__(self):

        self.supported_formats = (
            ".pdf",
            ".docx",
            ".txt"
        )

    # ======================================================
    # Read Uploaded Document
    # ======================================================

    def read_document(self, uploaded_file):

        if uploaded_file is None:
            raise ValueError("No document uploaded.")

        filename = uploaded_file.name
        extension = os.path.splitext(filename)[1].lower()

        if extension not in self.supported_formats:
            raise ValueError(
                f"Unsupported file format: {extension}\n"
                "Supported formats: PDF, DOCX, TXT"
            )

        if extension == ".pdf":
            return self.read_pdf(uploaded_file)

        elif extension == ".docx":
            return self.read_docx(uploaded_file)

        elif extension == ".txt":
            return self.read_txt(uploaded_file)

        return ""
    # ======================================================
    # Read PDF File
    # ======================================================

    def read_pdf(self, uploaded_file):

        text = ""

        try:

            pdf = PdfReader(uploaded_file)

            for page in pdf.pages:

                content = page.extract_text()

                if content:
                    text += content + "\n"

        except Exception as e:

            raise Exception(f"Unable to read PDF file: {e}")

        return text.strip()

    # ======================================================
    # Read DOCX File
    # ======================================================

    def read_docx(self, uploaded_file):

        text = ""

        try:

            document = Document(uploaded_file)

            for paragraph in document.paragraphs:

                if paragraph.text.strip():

                    text += paragraph.text.strip() + "\n"

        except Exception as e:

            raise Exception(f"Unable to read DOCX file: {e}")

        return text.strip()

    # ======================================================
    # Read TXT File
    # ======================================================

    def read_txt(self, uploaded_file):

        try:

            return uploaded_file.read().decode(
                "utf-8",
                errors="ignore"
            )

        except Exception as e:

            raise Exception(f"Unable to read TXT file: {e}")
    # ======================================================
    # Document Statistics
    # ======================================================

    def get_statistics(self, text):

        characters = len(text)
        words = len(text.split())
        lines = len(text.splitlines())

        return {
            "characters": characters,
            "words": words,
            "lines": lines
        }

    # ======================================================
    # Check Empty Document
    # ======================================================

    def is_empty(self, text):

        return len(text.strip()) == 0

    # ======================================================
    # Preview Document
    # ======================================================

    def get_preview(self, text, max_characters=500):

        if len(text) <= max_characters:
            return text

        return text[:max_characters] + "..."

    # ======================================================
    # File Information
    # ======================================================

    def get_file_info(self, uploaded_file):

        return {
            "filename": uploaded_file.name,
            "filesize_kb": round(uploaded_file.size / 1024, 2),
            "extension": os.path.splitext(uploaded_file.name)[1].lower()
        }