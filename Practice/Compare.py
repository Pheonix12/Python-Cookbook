import tkinter as tk
import langchain
import openai
import PyPDF2

def compare_pdfs(pdf_file1, pdf_file2):
  """Compares two PDF files using LangChain and OpenAI.

  Args:
    pdf_file1: The path to the first PDF file to compare.
    pdf_file2: The path to the second PDF file to compare.

  Returns:
    The difference between the two PDF files.
  """

  # Load the PDF files and extract the text.
  pdf1 = PyPDF2.PdfFileReader(pdf_file1)
  text1 = ""
  for page in pdf1.pages:
    text1 += page.extract_text()

  pdf2 = PyPDF2.PdfFileReader(pdf_file2)
  text2 = ""
  for page in pdf2.pages:
    text2 += page.extract_text()

  # Create a LangChain comparer.
  comparer = langchain.ComparerChain()

  # Compare the text of the two PDF files.
  difference = comparer(text1, text2)

  return difference

def main():
  root = tk.Tk()
  root.title("PDF Comparer")

  # Create a file dialog to select the first PDF file.
  pdf_file1 = tk.filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

  # Create a file dialog to select the second PDF file.
  pdf_file2 = tk.filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

  # Create a button to compare the PDF files.
  compare_button = tk.Button(root, text="Compare", command=lambda: compare(pdf_file1, pdf_file2))

  # Layout the widgets.
  pdf_file1_label = tk.Label(root, text="First PDF file:")
  pdf_file1_label.grid(row=0, column=0)
  pdf_file1_entry = tk.Entry(root)
  pdf_file1_entry.insert(0, pdf_file1)
  pdf_file1_entry.grid(row=0, column=1)

  pdf_file2_label = tk.Label(root, text="Second PDF file:")
  pdf_file2_label.grid(row=1, column=0)
  pdf_file2_entry = tk.Entry(root)
  pdf_file2_entry.insert(0, pdf_file2)
  pdf_file2_entry.grid(row=1, column=1)

  compare_button.grid(row=2, column=0, columnspan=2)

  root.mainloop()

def compare(pdf_file1, pdf_file2):
  difference = compare_pdfs(pdf_file1, pdf_file2)
  print(difference)

if __name__ == "__main__":
  main()
