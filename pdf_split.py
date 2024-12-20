from PyPDF2 import PdfFileReader, PdfFileWriter
import os

# Function to split PDF by character limit
def split_pdf_by_characters(input_path, output_folder, char_limit=60000):
    pdf = PdfFileReader(input_path)
    current_text = ""
    current_part = 1
    writer = PdfFileWriter()
    
    for page_num in range(pdf.getNumPages()):
        page = pdf.getPage(page_num)
        page_text = page.extract_text()
        current_text += page_text
        writer.addPage(page)
        
        if len(current_text) >= char_limit:
            output_path = os.path.join(output_folder, f"part_{current_part}.pdf")
            with open(output_path, "wb") as output_pdf:
                writer.write(output_pdf)
            writer = PdfFileWriter()
            current_text = ""
            current_part += 1
    
    # Write remaining content if any
    if current_text:
        output_path = os.path.join(output_folder, f"part_{current_part}.pdf")
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)

# Function to create output folder if it doesn't exist
def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Example usage
input_pdf_path = "path/to/your/input.pdf"
output_folder_path = "path/to/output/folder"
ensure_folder_exists(output_folder_path)
split_pdf_by_characters(input_pdf_path, output_folder_path)
