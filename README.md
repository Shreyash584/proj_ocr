# Text Extractor from Image using Tesseract OCR

This project is a Python-based tool that uses **Tesseract OCR** to extract text from image files. The program takes multiple image files as input, processes them, and outputs the extracted text into a `.txt` file stored in the same location as the image.

## Features

- Extracts text from images using Tesseract OCR.
- Supports multiple image file formats.
- Generates a `.txt` file with the extracted text, saved in the same folder as the image(s).
- Built with **OpenCV**, **NumPy**, **Tkinter**, and **Pytesseract**.

## Installation

To get started, you will need to have Python installed along with the following libraries:

- **Tesseract OCR** (Make sure to install Tesseract from [here](https://github.com/tesseract-ocr/tesseract)).
- **opencv-python** for image processing.
- **numpy** for array manipulation.
- **tkinter** for any GUI functionality.
- **pytesseract** for Tesseract bindings in Python.

To install the required libraries, you can use the following command:

```bash
pip install opencv-python numpy pytesseract
