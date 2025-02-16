*Text Extractor from Image using Tesseract OCR*

This project is a Python-based tool that uses Tesseract OCR to extract text from image files. The program takes multiple image files as input, processes them, and outputs the extracted text into a .txt file stored in the same location as the image.

#Features
Extracts text from images using Tesseract OCR.
Supports multiple image file formats.
Generates a .txt file with the extracted text, saved in the same folder as the image(s).
Built with OpenCV, NumPy, Tkinter, and Pytesseract.
Installation
To get started, you will need to have Python installed along with the following libraries:

Tesseract OCR (Make sure to install Tesseract from here).
opencv-python for image processing.
numpy for array manipulation.
tkinter for any GUI functionality.
pytesseract for Tesseract bindings in Python.
To install the required libraries, you can use the following command:

'pip install opencv-python numpy pytesseract'

Tesseract Installation
Before using the program, make sure to have Tesseract installed. You can download it from the following link based on your operating system:

Windows: Tesseract for Windows
macOS: brew install tesseract
Linux: sudo apt-get install tesseract-ocr
After installing Tesseract, ensure it's added to your system's PATH, or specify the path to the Tesseract executable in your code.

Usage
Place the image files you want to extract text from in a folder.
Run the script:
python text_extractor.py

The program will process all the images in the folder, extracting the text and saving it into .txt files with the same name as the image.
Example
If you have an image called example_image.png, the program will create a file called example_image.txt in the same directory with the extracted text.

Code Explanation
OpenCV is used to read the image and preprocess it (e.g., converting to grayscale, thresholding).
Pytesseract is used to apply OCR and extract the text from the processed image.
The extracted text is saved into a .txt file with the same name as the image.
Contributing
If you'd like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
