import PyPDF2
import openai
import tkinter as tk

def summarize_pdf(pdf_file_path):
  """Summarizes the text in a PDF file using ChatGPT."""

  pdf_file = open(pdf_file_path, 'rb')
  pdf_reader = PyPDF2.PdfReader(pdf_file)

  pdf_summary_text = ""
  for page_num in range(len(pdf_reader.pages)):
    page_text = pdf_reader.pages[page_num].extractText()

    # Summarize the page text using ChatGPT.
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        prompt="Summarize the following text: " + page_text,
        temperature=0.7,
        max_tokens=100)
    page_summary = response["choices"][0]["text"]

    pdf_summary_text += page_summary + "\n"

  return pdf_summary_text


root = tk.Tk()

def summarize():
  pdf_summary_text = summarize_pdf(root.tk.get("pdf_file_path"))
  tk.Label(root, text=pdf_summary_text).pack()

tk.Label(root, text="PDF file path:").pack()
tk.Entry(root, textvariable=root.tk.StringVar(), width=100).pack()
tk.Button(root, text="Summarize", command=summarize).pack()

root.mainloop()
