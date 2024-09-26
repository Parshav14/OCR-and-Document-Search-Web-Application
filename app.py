import cv2
import numpy as np
import pytesseract
import streamlit as st
from PIL import Image

# Configure pytesseract to use the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image):
    # Convert the uploaded image from numpy array to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to extract text from the image
    custom_config = r'--oem 3 --psm 6 -l eng+hin'  # Use both English and Hindi
    extracted_text = pytesseract.image_to_string(gray_image, config=custom_config)
    
    return extracted_text

def main():
    st.title("OCR and Document Search")
    st.write("Upload an image file for OCR processing.")

    # Upload image file
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Convert the file to an OpenCV format
        image = Image.open(uploaded_file)
        image_np = np.array(image)

        # Extract text from the image
        extracted_text = extract_text(image_np)

        st.subheader("Extracted Text:")
        st.write(extracted_text)

        # Keyword search functionality
        keyword = st.text_input("Enter a keyword to search within the extracted text:")
        
        if keyword:
            highlighted_text = extracted_text.replace(keyword, f"**{keyword}**")  # Simple highlighting
            st.subheader("Search Results:")
            st.write(highlighted_text)

if __name__ == "__main__":
    main()
