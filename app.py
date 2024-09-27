import streamlit as st
from PIL import Image
import numpy as np
import easyocr

# Set up the EasyOCR reader
reader = easyocr.Reader(['en', 'hi'], gpu=False)

# Add a custom background (replace with your own image link)
def add_bg_image():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://your-background-image-link.com");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_image()

# Title with styled colors and effects
st.markdown("<h1 style='text-align: center; color: #FF6347; font-family: sans-serif;'>✨SnapExtract - Accurate OCR✨</h1>", unsafe_allow_html=True)
st.write("<hr style='border:2px solid #FF6347;'>", unsafe_allow_html=True)

# Upload an image section
st.markdown("<h3 style='color: #4682B4; font-family: Arial;'>Upload an Image (PNG, JPG, JPEG):</h3>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image with a border and shadow effect
    img = Image.open(uploaded_file)
    st.markdown("<h4 style='color: #228B22; text-align: center;'>Uploaded Image:</h4>", unsafe_allow_html=True)
    st.image(img, caption="Your Image", use_column_width=True)

    # Convert image to numpy array for OCR
    img_array = np.array(img)

    # Extract text from the image
    extracted_text = reader.readtext(img_array, detail=0)
    final_text = " ".join(extracted_text)

    # Display the extracted text with custom styling
    st.markdown("<h3 style='color: #8A2BE2;'>Extracted Text:</h3>", unsafe_allow_html=True)
    st.write(f"<div style='background-color:#F0F8FF; padding:10px; border-radius:5px; color:#00008B;'>{final_text}</div>", unsafe_allow_html=True)

    # Keyword search input with custom font and placeholder
    # Displaying the keyword search label with HTML styling separately
    st.markdown("<h4 style='color:#FF4500;'>🔍 Enter a keyword to search in the extracted text:</h4>", unsafe_allow_html=True)

    # Keep the text input standard, without HTML
    search_keyword = st.text_input("Search for a keyword")

    # Keyword search result display with icons and dynamic color
    if search_keyword:
        if search_keyword.lower() in final_text.lower():
            st.markdown(f"<h4 style='color:green;'>✅ <b>Keyword found:</b> {search_keyword}</h4>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h4 style='color:red;'>❌ <b>Keyword '{search_keyword}' not found.</b></h4>", unsafe_allow_html=True)

else:
    st.markdown("<h4 style='text-align: center; color: grey;'>Please upload an image to extract text.</h4>", unsafe_allow_html=True)

# Footer section with 'Made with Love' and a heart symbol
st.markdown("<hr style='border:1px solid #FF6347;'>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center;'>
        <p style='color: #808080;'>Developed with ❤️ by Parshav Singla</a></p>
    </div>
    """, unsafe_allow_html=True)
