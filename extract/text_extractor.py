import pdfplumber

def extract_text_from_pdf(pdf_path):
    text_by_page = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                clean_text = " ".join(text.split())  # Remove \n and extra spaces
                text_by_page.append(clean_text)
            else:
                text_by_page.append("")
    return text_by_page
