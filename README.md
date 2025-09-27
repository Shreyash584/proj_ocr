📝TextVision

This project is a Python-based machine learning tool designed to recognize and extract handwritten text from images. The model is trained on a dataset of handwritten images and their corresponding ground-truth text files. It leverages Tesseract OCR with preprocessing via OpenCV and NumPy to improve recognition accuracy.

🔍 Project Overview

Trains a handwritten OCR model using labeled image data.

Extracts handwritten text from new images using Tesseract OCR.

Preprocesses images for optimal OCR performance.

Stores extracted text into .txt files named after the original images.

📁 Dataset Structure

Your training dataset should be structured as follows:

handwriting_data/
├── images/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── ground-truth/
    ├── image1.txt
    ├── image2.txt
    └── ...


Each .jpg file in the images/ folder should have a corresponding .txt file in ground-truth/ containing the actual handwritten text.

⚙️ Features

✅ Supports training on handwritten image datasets

📷 Image preprocessing using OpenCV (grayscale, thresholding, etc.)

🧠 Utilizes Tesseract OCR for text recognition

📄 Outputs recognized text into .txt files with the same name as the input image

🖼️ Easy integration with image datasets for batch processing

🧩 Installation

Before running the project, make sure to install all required dependencies:

1. Install Tesseract OCR

Windows: Download Tesseract for Windows

macOS:

brew install tesseract


Linux:

sudo apt-get install tesseract-ocr


Important:
Make sure Tesseract is added to your system's PATH. Alternatively, you can specify the Tesseract executable path in your code like this:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

2. Install Python Libraries

Install the required Python packages with:

pip install opencv-python numpy pytesseract

🚀 Usage

Prepare your dataset in the handwriting_data/ folder.

Ensure all images are in handwriting_data/images/ and their corresponding .txt files are in handwriting_data/ground-truth/.

Run the script:

python text_extractor.py


The program will:

Preprocess each image.

Use Tesseract to recognize handwritten text.

Output the recognized text into .txt files alongside the images.

🧪 Example

Given the following input:

Image: handwriting_data/images/sample01.jpg

Ground truth: handwriting_data/ground-truth/sample01.txt

The program will process sample01.jpg and create an output text file named sample01_output.txt (or similar), containing the recognized handwritten text.

🛠 Code Workflow

Image Loading – Uses OpenCV to load images.

Preprocessing – Applies grayscale conversion, denoising, thresholding, etc.

OCR – Uses Pytesseract to extract text from preprocessed images.

Output – Saves the recognized text into a .txt file for each image
