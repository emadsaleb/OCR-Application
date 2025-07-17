

 Document Scanner Application (OCR)

This is a simple OCR (Optical Character Recognition) web application built using Streamlit, Pytesseract, and Pillow. It allows users to upload an image (e.g., scanned documents or ID cards), and it extracts and displays key textual information from the image.



 Features

* Upload images in `.png`, `.jpg`, or `.jpeg` format.
* Automatically extract text using Tesseract OCR.
* Display:

  * Organization name (from the first two lines of extracted text)
  * Full name (from line 9)
  * Additional lines from the document

 Technologies Used

* Python 
* [Streamlit](https://streamlit.io/) - for the web interface
* [Pytesseract](https://pypi.org/project/pytesseract/) - wrapper for Tesseract OCR
* [Pillow (PIL)](https://pillow.readthedocs.io/) - for image handling
* [NumPy](https://numpy.org/) - to convert images into arrays



 Screenshot

![screenshot](https://user-images.githubusercontent.com/your-screenshot-placeholder.png)
Example of OCR extraction from an uploaded document


 Setup Instructions

 1. Clone the Repository

bash
git clone https://github.com/yourusername/ocr-streamlit-app.git
cd ocr-streamlit-app


 2. Install Dependencies

Create a virtual environment (optional) and install required packages:

bash
pip install -r requirements.txt


requirements.txt


streamlit
numpy
pytesseract
pillow


 3. Install Tesseract OCR

* Download from: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
* After installing, set the path in the script (already included):

python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


 4. Run the App

bash
streamlit run OCR.py


---

 Notes

* The script assumes the organization name is in the first two lines and the name is on the ninth line of the document. You may need to adjust `text_list` indexing depending on your specific document layout.
* Make sure the image contains clear and readable text for better OCR accuracy.



 Contact

For questions or suggestions, feel free to reach out:
Emad Salib Fahmy Ibrahim Boules
 [LinkedIn](https://www.linkedin.com/in/emad-salib-ab4968248)

Would you like me to export this into a `README.md` file or improve it further?
OCR-Application
