import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader
import openai

# OpenAI API credentials
openai.api_key = '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'


def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def generate_summary(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following text: {text}"},
        ],
        max_tokens=1000,
        temperature=0.3,
    )
    summary = response['choices'][0]['message']['content'].strip()
    return summary


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    if file_path:
        text = extract_text_from_pdf(file_path)
        summary = generate_summary(text)
        messagebox.showinfo('Summary', summary)


root = tk.Tk()
root.title("PDF Text Summarizer")

# GUI elements
label = tk.Label(root, text="Select a PDF file:")
label.pack(pady=10)

button = tk.Button(root, text="Browse", command=select_file)
button.pack(pady=5)

root.mainloop()
