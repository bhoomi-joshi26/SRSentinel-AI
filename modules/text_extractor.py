import PyPDF2
from docx import Document


class TextExtractor:

    def extract_text(self, uploaded_file):

        filename = uploaded_file.name.lower()

        if filename.endswith(".pdf"):
            return self.extract_pdf(uploaded_file)

        elif filename.endswith(".docx"):
            return self.extract_docx(uploaded_file)

        else:
            raise ValueError("Unsupported file format.")

    def extract_pdf(self, uploaded_file):

        reader = PyPDF2.PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    def extract_docx(self, uploaded_file):

        doc = Document(uploaded_file)

        text = ""

        for para in doc.paragraphs:

            text += para.text + "\n"

        return text