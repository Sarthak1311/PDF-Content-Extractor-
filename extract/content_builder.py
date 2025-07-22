import json

def build_json_output(text_pages, image_paths_by_page, output_path):
    structured_output = []
    
    for i, (text, images) in enumerate(zip(text_pages, image_paths_by_page), start=1):
        structured_output.append({
            "page": i,
            "text": text,
            "images": images
        })
    
    with open(output_path, "w") as json_file:
        json.dump(structured_output, json_file, indent=4)
