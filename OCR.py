import streamlit as st
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
st.title('Document Scanner Application')
def extract_text(img):
    text = pytesseract.image_to_string(img)
    return text
upload = st.file_uploader('Upload an Image....' , type = ['png' , 'jpg' , 'jpeg'])  
if upload is not None:
    img = Image.open(upload)
    img = np.array(img)
    st.image(img , caption = 'Uploaded Image')
    text = extract_text(img)
    #st.write(text)
    text_list = text.splitlines()
    #st.write(text_list)
    st.write('Oragnization Name:' , text_list[0] , ' ' , text_list[1])
    st.write("Name:" , text_list[8])
    st.write(text_list[3])
    st.write(text_list[4])
    st.write(text_list[5])
    st.write(text_list[6])
