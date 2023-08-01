import tkinter as tk
from docx2pdf import convert
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from pdf2docx import Converter

win = tk.Tk()
win.title("File Format Converter")


def openFile():
    file = askopenfile(filetypes=[('Word Files', '*.docx')])
    convert(file.name)
    showinfo("Done", "File Successfully Converted to PDF")


"""Firstly, we are filtering the files with pdf extension. Then we are replacing .pdf with .docx. After that we are 
initializing an instance of a class. Then we are starting the process and after that we are giving a message to the 
user."""


def convertPDFtoDOCX():
    pdf_file = askopenfile(filetypes=[('PDF Files', '*.pdf')])
    docx_file = pdf_file.name.replace(".pdf", ".docx")
    cv = Converter(pdf_file.name)
    cv.convert(docx_file)
    cv.close()
    showinfo("Done", "File Successfully Converted to DOCX")


# Formatting the window

label_choose_file = tk.Label(win, text="Choose File: ")
label_choose_file.grid(row=0, column=0, padx=5, pady=5)

button_select_word = ttk.Button(win, text="Select Word", width=30, command=openFile)
button_select_word.grid(row=0, column=1, padx=5, pady=5)

label_choose_pdf = tk.Label(win, text="Choose PDF: ")
label_choose_pdf.grid(row=1, column=0, padx=5, pady=5)

button_select_pdf = ttk.Button(win, text="Select PDF", width=30, command=convertPDFtoDOCX)
button_select_pdf.grid(row=1, column=1, padx=5, pady=5)

# Tkinter mainloop
win.mainloop()
