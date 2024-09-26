import streamlit as st
import easyocr
from PIL import Image

# Initialize EasyOCR Reader for English and Hindi
reader = easyocr.Reader(['en', 'hi'])

# Function to perform OCR on the uploaded image
def perform_ocr(image):
    # Convert image to RGB for processing
    image_rgb = image.convert("RGB")
    result = reader.readtext(image_rgb)
    
    # Extract text from result
    extracted_text = " ".join([text[1] for text in result])
    return extracted_text

# Function to search keywords in extracted text
def search_keywords(text, keywords):
    results = []
    for keyword in keywords:
        if keyword in text:
            results.append(keyword)
    return results

# Streamlit UI
st.title("OCR and Document Search Web Application")
st.write("Upload an image file (JPEG, PNG) containing text in Hindi and English.")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Perform OCR
    st.write("Performing OCR...")
    extracted_text = perform_ocr(image)
    
    st.subheader("Extracted Text:")
    st.write(extracted_text)
    
    # Keyword search
    st.subheader("Search in Extracted Text")
    keywords = st.text_input("Enter keywords (comma separated):")
    if st.button("Search"):
        if keywords:
            keywords_list = [k.strip() for k in keywords.split(",")]
            search_results = search_keywords(extracted_text, keywords_list)
            if search_results:
                st.write("Matching Keywords:")
                st.write(", ".join(search_results))
            else:
                st.write("No matches found.")
        else:
            st.write("Please enter keywords to search.")
