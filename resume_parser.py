import pymupdf


def extract_resume_text(uploaded_file):
    pdf_bytes = uploaded_file.read()

    document = fitz.open(stream=pdf_bytes, filetype="pdf")

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text
