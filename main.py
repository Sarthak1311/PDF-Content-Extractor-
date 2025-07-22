
import os
from extract.text_extractor import extract_text_from_pdf
from extract.image_extractor import extract_images_from_pdf
from extract.content_builder import build_json_output

def main():
    input_pdf = "/Users/sarthaktyagi/Desktop/pdf_question_generator/data /IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf"
    image_output_dir = "data/images"
    json_output_path = "output/extracted_data.json"

    os.makedirs("data/images", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    text_pages = extract_text_from_pdf(input_pdf)
    image_data = extract_images_from_pdf(input_pdf, image_output_dir)
    build_json_output(text_pages, image_data, json_output_path)

    print(f"✅ Extraction complete. JSON saved to {json_output_path}")

if __name__ == "__main__":
    main()
