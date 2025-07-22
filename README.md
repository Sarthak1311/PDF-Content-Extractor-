# PDF Content Extractor 

This project is a tool designed to extract **text** and **images** from educational PDFs such as Olympiad sample papers, and generate a **structured JSON** output that organizes the content page-by-page for downstream use like question answering or dataset preparation.

---

##  Features

-  Extracts **clean text** from each page of a PDF (removes `\n`).
-  Extracts **all images** from each page and saves them locally.
-  Generates a structured `JSON` file with:
  - Page number
  - Full page text (in one line)
  - Paths to all extracted images

---

##  Project Structure

```
pdf_question_generator/
│
├── data/
│   ├── input.pdf              # Input PDF file
│   └── images/                # Extracted images
│
├── output/
│   └── extracted_data.json    # Final structured JSON
│
├── extract/
│   ├── __init__.py
│   ├── text_extractor.py      # Extracts clean text
│   ├── image_extractor.py     # Extracts and saves images
│   └── content_builder.py     # Creates the final JSON output
│
├── main.py                    # Main runner script
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## 🧪Sample Output (`extracted_data.json`)

```json
[
  {
    "page": 1,
    "text": "CLASS 1 SAMPLE PAPER 1 SECTION-01 LOGICAL REASONING 1. Find the next figures in the figure pattern given below. [A] [B] [C] [D] Ans. [D] 2. Complete the number pattern. [A] [B] 1",
    "images": [
      "data/images/page1_image1.png",
      "data/images/page1_image2.png",
      "data/images/page1_image3.png"
    ]
  }
]
```

---

##  Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
PyMuPDF==1.22.5
pdfplumber==0.10.2
Pillow==10.2.0
```

---

##  How to Run

1. Place your target PDF file in the `data/` directory and rename it to `input.pdf`.

2. Run the main script:

```bash
python main.py
```

3. Check:
   - Extracted images in `data/images/`
   - Structured JSON in `output/extracted_data.json`

---

