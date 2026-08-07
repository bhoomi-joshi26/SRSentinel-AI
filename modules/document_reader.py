"""
===========================================================
SRSentinel AI
Document Reader Module
Supported Formats
• PDF
• DOCX
• TXT
===========================================================
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
    # --------------------------------------------------
    # Read Uploaded File
    # --------------------------------------------------
    def read_document(self, uploaded_file):
        if uploaded_file is None:
            raise ValueError("No document uploaded.")
        filename = uploaded_file.name
        extension = os.path.splitext(filename)[1].lower()
        if extension not in self.supported_formats:
            raise ValueError(
                f"Unsupported file format: {extension}\n"
                "Supported formats are: PDF, DOCX and TXT."
            )
        if extension == ".pdf":
            return self.read_pdf(uploaded_file)
        elif extension == ".docx":
            return self.read_docx(uploaded_file)
        elif extension == ".txt":
            return self.read_txt(uploaded_file)
    # --------------------------------------------------
    # Read PDF
    # --------------------------------------------------
    def read_pdf(self, uploaded_file):
        text = ""
        pdf = PdfReader(uploaded_file)
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        return text.strip()
    #---------------------------------------------------
    # Read DOCX
    # --------------------------------------------------
    def read_docx(self, uploaded_file):
        document = Document(uploaded_file)
        text = ""
        for paragraph in document.paragraphs:
             if paragraph.text.strip():
                 text += paragraph.text.strip() + "\n"
        return text.strip()
    # --------------------------------------------------
    # Read TXT
    # --------------------------------------------------
    def read_txt(self, uploaded_file):
        return uploaded_file.read().decode(
             "utf-8",
             errors="ignore" 
        )
    # --------------------------------------------------
    # Document Statistics
    # --------------------------------------------------
    def get_statistics(self, text):
        characters = len(text)
        words = len(text.split())
        lines = len(text.splitlines())
        return {
            "characters": characters,
            "words": words,
            "lines": lines
        }