import tkinter as tk
from tkinter import filedialog, Label, Text, Button, Frame, Canvas, Toplevel
import cv2
import pytesseract
from PIL import Image, ImageTk, ImageDraw
import os
import numpy as np
import pyttsx3  
from docx import Document
from pdf2image import convert_from_path

# Set the path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\path\to\poppler\bin"  # Update with the correct path

# Global variables
extracted_texts = ""
selected_lang = "eng"
selected_file_name = ""

# Text-to-speech engine
engine = pyttsx3.init()

# Custom Colors & Fonts
PRIMARY_COLOR = "#0F2027"
SECONDARY_COLOR = "#2C5364"
ACCENT_COLOR = "#00C9FF"
BUTTON_COLOR = "#38ef7d"
DANGER_COLOR = "#FF5858"
TEXT_COLOR = "#F5F5F5"
CARD_BG = "#212121"
FONT_BOLD = ("Segoe UI", 13, "bold")
FONT_REGULAR = ("Segoe UI", 11)

def extract_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(gray, lang=selected_lang)
    return text.strip()

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    texts = []
    for img in images:
        text = pytesseract.image_to_string(img, lang=selected_lang)
        texts.append(text.strip())
    return "\n".join(texts)

def select_files():
    global extracted_texts, selected_file_name
    file_paths = filedialog.askopenfilenames(
        filetypes=[("Image & PDF Files", "*.jpg;*.png;*.jpeg;*.pdf")]
    )
    if not file_paths:
        return
    
    extracted_texts = ""
    selected_file_name = os.path.basename(file_paths[0])  
    
    loading_popup("Extracting text...")  # Show loading spinner
    
    for file_path in file_paths:
        if file_path.lower().endswith(".pdf"):
            texts = extract_text_from_pdf(file_path)
        else:
            texts = extract_text(file_path)
        extracted_texts += texts + "\n" + "-"*40 + "\n"
    
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, extracted_texts)
    file_name_label.config(text=f"File: {selected_file_name}")  
    close_loading_popup()  # Hide loading spinner

def save_text_to_file():
    edited_text = text_box.get("1.0", tk.END).strip()
    if not edited_text:
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(edited_text)
        show_toast("Saved as TXT!")

def save_text_to_word():
    edited_text = text_box.get("1.0", tk.END).strip()
    if not edited_text:
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Document", "*.docx")])
    if file_path:
        doc = Document()
        doc.add_paragraph(edited_text)
        doc.save(file_path)
        show_toast("Saved as DOCX!")

def text_to_speech():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()
        show_toast("Speaking...")

# Toast Message
def show_toast(msg):
    toast = Toplevel(root)
    toast.overrideredirect(True)
    toast.configure(bg=SECONDARY_COLOR)
    toast.geometry(f"220x40+{root.winfo_x()+240}+{root.winfo_y()+620}")
    Label(toast, text=msg, bg=SECONDARY_COLOR, fg=TEXT_COLOR, font=FONT_REGULAR).pack(expand=True)
    toast.after(1000, toast.destroy)

# Loading Spinner
loading_win = None
def loading_popup(msg):
    global loading_win
    loading_win = Toplevel(root)
    loading_win.overrideredirect(True)
    loading_win.configure(bg=SECONDARY_COLOR)
    loading_win.geometry(f"220x70+{root.winfo_x()+240}+{root.winfo_y()+330}")
    Label(loading_win, text=msg, bg=SECONDARY_COLOR, fg=ACCENT_COLOR, font=FONT_BOLD).pack(pady=20)
    loading_win.update_idletasks()

def close_loading_popup():
    global loading_win
    if loading_win:
        loading_win.destroy()
        loading_win = None

# Gradient background using Canvas
def create_gradient(canvas, width, height, color1, color2):
    gradient = Image.new("RGB", (width, height), color1)
    draw = ImageDraw.Draw(gradient)
    for i in range(height):
        ratio = i / height
        r = int((1-ratio)*int(color1[1:3],16) + ratio*int(color2[1:3],16))
        g = int((1-ratio)*int(color1[3:5],16) + ratio*int(color2[3:5],16))
        b = int((1-ratio)*int(color1[5:7],16) + ratio*int(color2[5:7],16))
        draw.line([(0, i), (width, i)], fill=(r,g,b))
    gradient_img = ImageTk.PhotoImage(gradient)
    canvas.create_image(0, 0, anchor="nw", image=gradient_img)
    canvas.gradient_img = gradient_img

root = tk.Tk()
root.title("TextVision")
root.geometry("750x750")
root.resizable(False, False)

# Gradient background
bg_canvas = Canvas(root, width=750, height=750, highlightthickness=0)
bg_canvas.place(x=0, y=0)
create_gradient(bg_canvas, 750, 750, PRIMARY_COLOR, SECONDARY_COLOR)

# Welcome Frame
welcome_frame = Frame(root, bg=PRIMARY_COLOR)
welcome_frame.place(relwidth=1, relheight=1)

logo_path = r"D:\Academics\Text Extracting Using OCR\Screenshot_2025-03-12_130414-removebg-preview.png"
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((180, 160), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

Label(welcome_frame, image=logo_photo, bg=PRIMARY_COLOR).pack(pady=60)
Label(welcome_frame, text="TextVision", fg=ACCENT_COLOR, bg=PRIMARY_COLOR, font=("Segoe UI", 22, "bold")).pack(pady=0)
Label(welcome_frame, text="by Shreyash Killedar", fg="gray", bg=PRIMARY_COLOR, font=("Segoe UI", 10, "italic")).pack(pady=2)

Button(welcome_frame, text="Extract Text From Images", command=lambda: switch_frame(main_frame), 
       bg=BUTTON_COLOR, fg="black", font=FONT_BOLD, relief="flat", padx=15, pady=8, bd=0, highlightthickness=0).pack(pady=20)

Button(welcome_frame, text="Feature 1", bg=ACCENT_COLOR, fg="black", font=FONT_BOLD, relief="flat", padx=15, pady=8, bd=0, highlightthickness=0).pack(pady=5)
Button(welcome_frame, text="Feature 2", bg=ACCENT_COLOR, fg="black", font=FONT_BOLD, relief="flat", padx=15, pady=8, bd=0, highlightthickness=0).pack(pady=5)

# Main Frame (Hidden initially)
main_frame = Frame(root, bg=CARD_BG)

def switch_frame(frame):
    frame.tkraise()

for frame in (welcome_frame, main_frame):
    frame.place(relwidth=1, relheight=1)

# Card Container
card = Frame(main_frame, bg=CARD_BG, bd=2, relief="groove")
card.place(relx=0.5, rely=0.12, anchor="n", width=600, height=520)

Label(card, text="Select Files", fg=ACCENT_COLOR, bg=CARD_BG, font=FONT_BOLD).pack(pady=10)
Button(card, text="Browse Files", command=select_files, bg=BUTTON_COLOR, fg="black", font=FONT_BOLD, relief="flat", padx=10, pady=5, bd=0).pack(pady=5)

file_name_label = Label(card, text="", fg=ACCENT_COLOR, bg=CARD_BG, font=("Segoe UI", 10, "italic"))
file_name_label.pack()

Label(card, text="Extracted Text:", fg=TEXT_COLOR, bg=CARD_BG, font=FONT_BOLD).pack(pady=10)
text_box = Text(card, height=12, width=60, bg="#333", fg="white", font=FONT_REGULAR, bd=2, relief="flat", insertbackground=ACCENT_COLOR)
text_box.pack(pady=10)

button_frame = Frame(card, bg=CARD_BG)
button_frame.pack(pady=10)

Button(button_frame, text="Save as TXT", command=save_text_to_file, bg=ACCENT_COLOR, fg="black", font=FONT_BOLD, relief="flat", padx=10, bd=0).pack(side=tk.LEFT, padx=8)
Button(button_frame, text="Save as DOCX", command=save_text_to_word, bg=ACCENT_COLOR, fg="black", font=FONT_BOLD, relief="flat", padx=10, bd=0).pack(side=tk.LEFT, padx=8)
Button(button_frame, text="Speak", command=text_to_speech, bg=BUTTON_COLOR, fg="black", font=FONT_BOLD, relief="flat", padx=10, bd=0).pack(side=tk.LEFT, padx=8)

Button(main_frame, text="Back to Home", command=lambda: switch_frame(welcome_frame), 
       bg=DANGER_COLOR, fg="white", font=FONT_BOLD, relief="flat", padx=10, pady=5, bd=0).place(relx=0.5, rely=0.86, anchor="center")

switch_frame(welcome_frame)
root.mainloop()