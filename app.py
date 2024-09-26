import os
import pytesseract
import streamlit as st
from PIL import Image

# Set Tesseract path
tesseract_path = os.environ.get('TESSERACT_PATH')
if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    st.error("Tesseract executable not found. Please set the TESSERACT_PATH environment variable.")

def extract_text(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    extracted_text = pytesseract.image_to_string(gray_image)
    return extracted_text

def main():
    st.title("OCR Application")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image_np = np.array(image)
        extracted_text = extract_text(image_np)
        st.write("Extracted Text:")
        st.write(extracted_text)

if __name__ == "__main__":
    main()
