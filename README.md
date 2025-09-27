# 📝 TextVision

**TextVision** is a Python-based machine learning tool designed to recognize and extract handwritten text from images. It leverages Tesseract OCR, enhanced by image preprocessing with OpenCV and NumPy, to improve recognition accuracy.

---

## 🔍 Project Overview

- Trains a handwritten OCR model using labeled image data.
- Extracts handwritten text from new images using Tesseract OCR.
- Preprocesses images for optimal OCR performance.
- Stores extracted text into `.txt` files named after the original images.

---

## 📁 Dataset Structure

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


yaml
Copy code

> Each `.jpg` file in the `images/` folder should have a corresponding `.txt` file in `ground-truth/` containing the actual handwritten text.

---

## ⚙️ Features

- ✅ Supports training on handwritten image datasets
- 📷 Image preprocessing using OpenCV (grayscale, thresholding, etc.)
- 🧠 Utilizes Tesseract OCR for text recognition
- 📄 Outputs recognized text into `.txt` files with the same name as the input image
- 🖼️ Easy integration with image datasets for batch processing

---
