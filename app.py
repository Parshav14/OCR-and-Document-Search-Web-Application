import cv2
import numpy as np
import pytesseract
import streamlit as st
from PIL import Image
import re

# Configure pytesseract to use the Tesseract executable path if needed
# Uncomment the following line if you need to set a specific Tesseract path
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def extract_text(image):
    """Extract text from the image using pytesseract."""
    # Convert the uploaded image to grayscale
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    
    # Use pytesseract to extract text from the grayscale image
    custom_config = r'--oem 3 --psm 6 -l eng+hin'  # Use both English and Hindi
    extracted_text = pytesseract.image_to_string(gray_image, config=custom_config)
    
    return extracted_text.strip()  # Return stripped text to clean output

def highlight_text(text, keyword):
    """Highlight the matching keyword in the extracted text."""
    if keyword:
        highlighted_text = re.sub(f"({re.escape(keyword)})", r'<mark>\1</mark>', text, flags=re.IGNORECASE)
        return highlighted_text
    return text

# Streamlit app layout
st.set_page_config(page_title="OCR and Document Search", layout="wide")
st.title("📄 OCR and Document Search")
st.write("Upload an image containing Hindi and English text to extract and search.")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Extract text
    extracted_text = extract_text(image)
    
    if extracted_text:
        st.subheader("📝 Extracted Text:")
        st.write(extracted_text)

        # Keyword search
        keyword = st.text_input("🔍 Enter keyword to search in extracted text:")
        
        if keyword:
            highlighted_output = highlight_text(extracted_text, keyword)
            st.subheader("🔍 Search Results:")
            st.markdown(highlighted_output, unsafe_allow_html=True)
    else:
        st.warning("⚠️ No text detected. Please try a clearer image.")

