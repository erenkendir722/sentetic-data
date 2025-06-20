from utils.pdf_utils import convert_pdf_to_text
from utils.llm_utils import generate_qa

if __name__ == "__main__":
    pdf_path = "data/pdf/rapor.pdf"
    text = convert_pdf_to_text(pdf_path)

    qa_pairs = generate_qa(text, num_questions=10)
    
    for i, pair in enumerate(qa_pairs, 1):
        print(f"{i}. Q: {pair.get('question')}\n   A: {pair.get('answer')}\n")
