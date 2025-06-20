from pdfminer.high_level import extract_text

def convert_pdf_to_text(pdf_path):
    text = extract_text(pdf_path)
    return text.strip()
