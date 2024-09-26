import cv2
import numpy as np
import pytesseract
import streamlit as st
from PIL import Image

# Set the Tesseract executable path
import pytesseract

# Set the Tesseract executable path for Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image):
    # Convert the uploaded image to grayscale
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    
    # Use pytesseract to extract text from the image
    custom_config = r'--oem 3 --psm 6 -l eng+hin'  # Both English and Hindi
    extracted_text = pytesseract.image_to_string(gray_image, config=custom_config)
    
    return extracted_text

# Streamlit application layout
st.title("OCR and Document Search")
uploaded_file = st.file_uploader("Upload an image file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open the image file
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Extract text
    extracted_text = extract_text(image)
    st.subheader("Extracted Text")
    st.write(extracted_text)

    # Search functionality
    keyword = st.text_input("Enter keyword to search:")
    if keyword:
        if keyword.lower() in extracted_text.lower():
            st.success(f"Keyword '{keyword}' found in the extracted text!")
        else:
            st.error(f"Keyword '{keyword}' not found in the extracted text.")
