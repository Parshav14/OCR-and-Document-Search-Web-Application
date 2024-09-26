import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import streamlit as st
from PIL import Image

# Set the Tesseract command path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image):
    # Convert the uploaded image from numpy array to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use pytesseract to extract text from the image
    custom_config = r'--oem 3 --psm 6 -l eng+hin'  # Use both English and Hindi
    extracted_text = pytesseract.image_to_string(gray_image, config=custom_config)
    
    return extracted_text

# Streamlit app
def main():
    st.title("OCR and Document Search")
    
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Open the image file and convert it to a format suitable for OpenCV
        image = Image.open(uploaded_file)
        image_np = np.array(image)

        # Extract text from the image
        extracted_text = extract_text(image_np)
        
        # Display the extracted text
        st.subheader("Extracted Text:")
        st.write(extracted_text)
        
        # Keyword search
        keyword = st.text_input("Enter keyword to search:")
        if keyword:
            matches = [line for line in extracted_text.split('\n') if keyword.lower() in line.lower()]
            st.subheader("Search Results:")
            for match in matches:
                st.write(match)

if __name__ == "__main__":
    main()
