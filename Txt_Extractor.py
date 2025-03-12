import tkinter as tk
from tkinter import filedialog, Label, Text, Button
import cv2
import pytesseract
from PIL import Image, ImageTk
import os
import numpy as np
from docx import Document
from pdf2image import convert_from_path

# Set the path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Global variables
extracted_texts = ""
image_folder = ""
selected_lang = "eng"
POPPLER_PATH = r"C:\path\to\poppler\bin"  # Update with the correct path

# Function to open file dialog and select multiple images or PDFs
def select_files():
    global extracted_texts, image_folder
    file_paths = filedialog.askopenfilenames(filetypes=[("Image & PDF Files", "*.jpg;*.png;*.jpeg;*.pdf")])
    if not file_paths:
        return
    
    extracted_texts = ""
    for file_path in file_paths:
        if file_path.lower().endswith(".pdf"):
            texts = extract_text_from_pdf(file_path)
        else:
            texts = extract_text(file_path)
        
        image_name = os.path.basename(file_path)
        formatted_text = f"Name: {image_name}\nExtracted Text:\n{texts}\n{'-'*40}\n"
        extracted_texts += formatted_text
    
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, extracted_texts)
    image_folder = os.path.dirname(file_paths[0])

# Function to extract text from image
def extract_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(gray, lang=selected_lang)
    return text.strip()

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    texts = []
    for img in images:
        text = pytesseract.image_to_string(img, lang=selected_lang)
        texts.append(text.strip())
    return "\n".join(texts)

# Function to save extracted text as a TXT file
def save_text_to_file():
    global extracted_texts, image_folder
    if not extracted_texts:
        return
    file_path = os.path.join(image_folder, "extracted_texts.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(extracted_texts)

# Function to save extracted text as a Word file
def save_text_to_word():
    global extracted_texts, image_folder
    if not extracted_texts:
        return
    file_path = os.path.join(image_folder, "extracted_texts.docx")
    doc = Document()
    doc.add_paragraph(extracted_texts)
    doc.save(file_path)

# Create GUI Window
root = tk.Tk()
root.title("Text Extractor")
root.geometry("700x700")
root.configure(bg="#2C3E50")

button_style = {"bg": "#3498DB", "fg": "white", "font": ("Arial", 12, "bold"), "relief": "flat", "padx": 10, "pady": 5}
label_style = {"bg": "#2C3E50", "fg": "white", "font": ("Arial", 12, "bold")}

Label(root, text="Select Files:", **label_style).pack(pady=10)
Button(root, text="Browse Files", command=select_files, **button_style).pack(pady=5)

Label(root, text="Extracted Text:", **label_style).pack(pady=10)
text_box = Text(root, height=12, width=60, bg="#34495E", fg="white", font=("Arial", 11))
text_box.pack(pady=10)

button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack(pady=10)

Button(button_frame, text="Save as Text File", command=save_text_to_file, **button_style).pack(side=tk.LEFT, padx=5)
Button(button_frame, text="Save as Word File", command=save_text_to_word, **button_style).pack(side=tk.LEFT, padx=5)

# Add logo
logo_path = r"D:\Academics\Text Extracting Using OCR\Screenshot_2025-03-12_130414-removebg-preview.png"
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((200, 180), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = Label(root, image=logo_photo, bg="#2C3E50")
logo_label.image = logo_photo
logo_label.pack(side=tk.BOTTOM, pady=30)
#Label(root, text="Made by SHREYASH KILLEDAR", bg="#2C3E50", fg="white", font=("Arial", 7, "italic")).pack(side=tk.BOTTOM, pady=5)
# Run the GUI
root.mainloop()
