
import streamlit as st
from PIL import Image
import pytesseract

# Title of the app
st.title("OCR and Keyword Search Web Application")

# Upload an image file
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Extract text from the image using OCR
    custom_config = r'--oem 3 --psm 6 -l eng+hin'
    extracted_text = pytesseract.image_to_string(img, config=custom_config)

    # Display the extracted text
    st.subheader("Extracted Text:")
    st.write(extracted_text)

    # Keyword search functionality
    search_keyword = st.text_input("Enter a keyword to search in the extracted text:")
    if search_keyword:
        if search_keyword.lower() in extracted_text.lower():
            st.markdown(f"**Keyword found:** {search_keyword}")
            # Highlighting the matched keyword in the text
            st.write(extracted_text.replace(search_keyword, f"**{search_keyword}**"))
        else:
            st.write("Keyword not found.")
            
