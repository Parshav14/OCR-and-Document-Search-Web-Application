import streamlit as st
import easyocr
from PIL import Image

# Function to add a background image for enhanced design
def add_bg_image(bg_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({bg_url});
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """, unsafe_allow_html=True
    )

# Set a background image (you can replace the URL with your local path if needed)
add_bg_image("https://your-background-image-link.com/background.jpg")

# Title of the app with enhanced design
st.markdown("<h1 style='text-align: center; color: orange;'>OCR and Keyword Search Web Application</h1>", unsafe_allow_html=True)
st.write("---")

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

# Upload an image file
uploaded_file = st.file_uploader("Upload an Image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    # Perform OCR
    st.write("Performing OCR...")
    extracted_text = perform_ocr(img)
    
    # Display extracted text with a collapsible section
    with st.expander("Extracted Text"):
        st.write(extracted_text)
    
    # Keyword search functionality
    search_keywords = st.text_input("Enter keywords (comma separated):")
    if st.button("Search"):
        if search_keywords:
            keywords_list = [k.strip() for k in search_keywords.split(",")]
            matching_keywords = [keyword for keyword in keywords_list if keyword in extracted_text]
            if matching_keywords:
                st.markdown(f"<p style='color: green;'>✅ **Matching Keywords:** {', '.join(matching_keywords)}</p>", unsafe_allow_html=True)
                
                # Highlight matched keywords in the extracted text
                highlighted_text = extracted_text
                for keyword in matching_keywords:
                    highlighted_text = highlighted_text.replace(keyword, f"**{keyword}**")
                st.write(highlighted_text)
            else:
                st.markdown("<p style='color: red;'>❌ No matches found.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color: red;'>❌ Please enter keywords to search.</p>", unsafe_allow_html=True)

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
