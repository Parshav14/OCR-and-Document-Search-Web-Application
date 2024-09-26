import streamlit as st
from PIL import Image
import numpy as np
import easyocr

# Initialize EasyOCR Reader for Hindi and English languages
reader = easyocr.Reader(['en', 'hi'], gpu=False)  # Disable GPU if you're on a CPU-only environment

# Title of the App
st.title("Accurate OCR for English and Hindi")
st.write("---")

# File uploader to accept images
uploaded_file = st.file_uploader("Upload an Image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open the image using PIL
    img = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Extract text from the image using EasyOCR
    extracted_text = reader.readtext(img_array, detail=0)  # Set detail=0 to get only the text
    
    # Join the extracted text into a single string
    final_text = " ".join(extracted_text)

    # Display the extracted text
    st.subheader("Extracted Text")
    st.write(final_text)

    # Keyword search functionality
    search_keyword = st.text_input("Enter a keyword to search in the extracted text:")
    if search_keyword:
        if search_keyword.lower() in final_text.lower():
            st.success(f"✅ Keyword found: {search_keyword}")
        else:
            st.error(f"❌ Keyword '{search_keyword}' not found.")

else:
    st.markdown("<h4 style='text-align: center; color: grey;'>Please upload an image to extract text.</h4>", unsafe_allow_html=True)
