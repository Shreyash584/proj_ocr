import tkinter as tk
from tkinter import filedialog, Label, Text, Button
import cv2
import pytesseract
from PIL import Image, ImageTk
import os

# Set the path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to open file dialog and select multiple images
def select_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if not file_paths:
        return  # No files selected
    
    # Display the first selected image
    display_image(file_paths[0])

    # Extract text from all selected images
    extracted_texts = []
    for file_path in file_paths:
        text = extract_text(file_path)
        image_name = os.path.basename(file_path)  # Get only the image name
        formatted_text = f"Name: {image_name}\nExtracted Text:\n{text}\n{'-'*40}\n"
        extracted_texts.append(formatted_text)

    # Combine all text and show in text box
    full_text = "\n".join(extracted_texts)
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, full_text)

    # Get folder of first image and save the extracted text there
    image_folder = os.path.dirname(file_paths[0])
    save_text_to_file(full_text, image_folder)

# Function to display image in GUI
def display_image(image_path):
    img = Image.open(image_path)
    img = img.resize((300, 300), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

# Function to extract text from an image
def extract_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()

# Function to save extracted text to a file in the image folder
def save_text_to_file(text, folder_path):
    file_path = os.path.join(folder_path, "extracted_texts.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Text saved at: {file_path}")  # Debugging: Check if the file is created

# Create GUI Window
root = tk.Tk()
root.title("Text Extractor")
root.geometry("700x600")
root.configure(bg="#2C3E50")  # Dark blue-gray background

# Custom Styles
button_style = {"bg": "#3498DB", "fg": "white", "font": ("Arial", 12, "bold"), "relief": "flat", "padx": 10, "pady": 5}
label_style = {"bg": "#2C3E50", "fg": "white", "font": ("Arial", 12, "bold")}

# Add UI elements
Label(root, text="Select Images:", **label_style).pack(pady=10)
Button(root, text="Browse Images", command=select_images, **button_style).pack(pady=5)

image_label = Label(root, bg="#2C3E50")
image_label.pack()

Label(root, text="Extracted Text:", **label_style).pack(pady=10)
text_box = Text(root, height=12, width=60, bg="#34495E", fg="white", font=("Arial", 11))
text_box.pack(pady=10)

# Large Centered DYPCET Watermark
watermark_label = Label(root, text="DYPCET", font=("Arial", 24, "bold"), bg="#2C3E50", fg="white")
watermark_label.pack(side="bottom", pady=40)

# Bottom-right corner author name
author_label = Label(root, text="By Shrey K", font=("Arial", 10, "bold"), bg="#2C3E50", fg="white")
author_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)  # Bottom right corner

# Run the GUI
root.mainloop()
