import difflib
import PyPDF2
import tkinter as tk
from tkinter import filedialog
import openai

# Set up OpenAI API credentials
openai.api_key = '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'

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

def compare_pdf_files(file1, file2):
    text1 = extract_text_from_pdf(file1)
    text2 = extract_text_from_pdf(file2)

    #GPT-3.5 Turbo
    prompt = f"Differences between {file1} and {file2}:"
    input_text = prompt + '\n' + text1 + '\n' + text2
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )
    comparison = response.choices[0].text.strip()

    return comparison

def browse_file(label):
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    label.config(text=file_path)

def compare_files():
    file1 = label1.cget("text")
    file2 = label2.cget("text")

    if file1 and file2:
        differences = compare_pdf_files(file1, file2)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, differences)
    else:
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, "Please select two PDF files.")

# Create main window
window = tk.Tk()
window.title("PDF Comparison Tool")

# file selection buttons and labels
label1 = tk.Label(window, text="")
label1.pack()
button1 = tk.Button(window, text="Select PDF File 1", command=lambda: browse_file(label1))
button1.pack()

label2 = tk.Label(window, text="")
label2.pack()
button2 = tk.Button(window, text="Select PDF File 2", command=lambda: browse_file(label2))
button2.pack()

#ompare button
compare_button = tk.Button(window, text="Compare", command=compare_files)
compare_button.pack()

#output text box
text_output = tk.Text(window, height=10, width=50)
text_output.pack()


window.mainloop()
