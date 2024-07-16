import os
import fitz  # PyMuPDF
import json


def pdf_to_json(pdf_path):
    document = fitz.open(pdf_path)
    pdf_content = {}
    
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text("text")
        pdf_content[f"Page_{page_num + 1}"] = text.strip()

    return pdf_content


def save_json(content, json_path):
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(content, json_file, ensure_ascii=False, indent=4)


def main():
    pdf_dir = os.path.join('resources', 'PDFS')
    for file_name in os.listdir(pdf_dir):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, file_name)
            json_path = os.path.splitext(pdf_path)[0] + '.json'
            
            pdf_content = pdf_to_json(pdf_path)
            save_json(pdf_content, json_path)
            print(f"Converted {file_name} to JSON and saved as {json_path}")


if __name__ == '__main__':
    main()
