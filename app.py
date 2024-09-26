import streamlit as st
from PIL import Image
import easyocr

# Function to add a background image for enhanced design
def add_bg_image(bg_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({bg_url});
            background-size: cover;
        }}
        </style>
        """, unsafe_allow_html=True
    )

# Set a background image
add_bg_image("https://your-background-image-link.com/background.jpg")

# Title of the app
st.markdown("<h1 style='text-align: center; color: orange;'>OCR and Keyword Search Web Application (EasyOCR)</h1>", unsafe_allow_html=True)
st.write("---")

# Upload an image file
uploaded_file = st.file_uploader("Upload an Image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Initialize EasyOCR reader (English and Hindi in this case)
    reader = easyocr.Reader(['en', 'hi'])  # Add languages as needed
    
    # Extract text from the image using EasyOCR
    extracted_text = reader.readtext(uploaded_file, detail=0)  # detail=0 to get only the text, not box info
    
    # Combine the extracted text into a single string
    extracted_text_str = " ".join(extracted_text)
    
    # Display the extracted text in a collapsible section
    with st.expander("Extracted Text"):
        st.write(extracted_text_str)
    
    # Keyword search functionality
    search_keyword = st.text_input("Enter a keyword to search in the extracted text:")
    if search_keyword:
        if search_keyword.lower() in extracted_text_str.lower():
            st.markdown(f"<p style='color: green;'>✅ **Keyword found:** {search_keyword}</p>", unsafe_allow_html=True)
            
            # Highlight matched keywords in the extracted text
            highlighted_text = extracted_text_str.replace(search_keyword, f"**{search_keyword}**")
            st.write(highlighted_text)
        else:
            st.markdown("<p style='color: red;'>❌ Keyword not found.</p>", unsafe_allow_html=True)

else:
    st.markdown("<h4 style='text-align: center; color: grey;'>Please upload an image to begin OCR and search.</h4>", unsafe_allow_html=True)

# Footer section with additional info
st.markdown("""
    <hr>
    <div style='text-align: center;'>
        <p style='color: grey;'>Developed by <a href='https://your-portfolio-link.com' target='_blank'>Your Name</a></p>
        <p style='color: grey;'>Hoping to be at IITR soon for internship!</p>
    </div>
    """, unsafe_allow_html=True)
