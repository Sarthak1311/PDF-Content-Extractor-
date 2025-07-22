import fitz  
import os

def extract_images_from_pdf(pdf_path, output_dir):
    doc = fitz.open(pdf_path)
    image_data = []

    os.makedirs(output_dir, exist_ok=True)

    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        images = page.get_images(full=True)
        page_images = []

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"page{page_number + 1}_image{img_index + 1}.{image_ext}"
            image_path = os.path.join(output_dir, image_filename)

            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)

            page_images.append(image_path)

        image_data.append(page_images)
    
    return image_data
