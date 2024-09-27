# 📜 SnapExtract - Accurate OCR 🖼️✨

Welcome to **SnapExtract** – an intuitive web application that extracts text from images with high accuracy, supporting both **English** and **Hindi** languages. This tool allows users to upload images, extract text, and search for specific keywords within the extracted text, all wrapped in a stylish and interactive interface. 

---

## 🚀 Project Overview

**SnapExtract** leverages the power of **EasyOCR** to extract text from uploaded images, enabling users to retrieve and search text in a hassle-free manner. It supports both **English** and **Hindi** OCR functionalities and offers a user-friendly interface built using **Streamlit**.

### 🌟 Key Features:
- **Multi-language Support**: OCR for both **English** and **Hindi** text.
- **Keyword Search**: Quickly search for keywords within the extracted text.
- **Intuitive Design**: Modern UI for a seamless user experience with stylish fonts, background images, and effects.
- **Real-time Feedback**: Immediate display of extracted text and search results.
- **Optimized Performance**: Memory-efficient operations for smoother functionality.

---

## 📁 Deliverables

### 🧑‍💻 Code Submission:
- **Python Scripts**:
    - The web app source code, including the OCR processing and search functionality, is implemented in the `app.py` script.
    - The application leverages **Streamlit** for the frontend interface and **EasyOCR** for text extraction.
- **Environment Setup**:
    - A `requirements.txt` file for installing the necessary dependencies.
    - A detailed `README.md` file (this file) to guide through the setup, running, and deployment processes.

### 🌐 Live Web Application:
- A live URL of the deployed application (deployed on **Streamlit Cloud**) where users can upload images, extract text, and test the search functionality.
    - [Live App URL] – Click here to visit and test the application!

### 📜 Extracted Text and Search Output:
- The application will display the extracted text in the web interface after uploading an image.
- The search functionality will provide immediate feedback if the keyword is found within the extracted text.

---

## ⚙️ Setup & Installation Guide

### 📥 Prerequisites
- **Python 3.8+** is required to run this project locally.
- Install the following libraries:
  - `easyocr`
  - `streamlit`
  - `Pillow`
  - `numpy`

### 🛠️ Installation Steps
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repo/snapextract.git
    cd snapextract
    ```

2. **Install Required Packages**:
    Run the following command to install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application Locally**:
    Use the following command to launch the Streamlit app:
    ```bash
    streamlit run app.py
    ```
    This will launch the application locally, accessible in your browser at `http://localhost:8501`.

### 🧪 Running the App:
1. Open your browser and go to the local URL displayed in the terminal.
2. Upload an image (JPG, PNG, JPEG) that contains text.
3. Extracted text will be displayed in the **Extracted Text** section.
4. Enter a keyword to search within the extracted text.

---

## 🚀 Deployment Process

You can deploy **SnapExtract** using **Streamlit Cloud** or other cloud platforms. Below are the steps for deploying on **Streamlit Cloud**.

### 🌐 Streamlit Cloud Deployment:
1. **Create a New Streamlit Cloud Account** (if you don't have one):  
    Visit [Streamlit Cloud](https://streamlit.io/cloud) and create an account.
    
2. **Upload the Project Repository**:  
    Connect your GitHub account and select the repository containing your project.

3. **Deployment Configuration**:  
    Set the correct branch and main script (`app.py`), and the platform will handle the deployment automatically.

4. **Obtain the Live URL**:  
    Once deployed, you'll receive a live URL to access your web application. Share this URL with users for testing.

---

## 📊 Results Section

In this section, you'll find screenshots and sample results from the **SnapExtract** portal. Below are some examples showcasing the OCR extraction and keyword search functionalities.

### 📸 Example 1: SnapExtract
![English Text Extraction](https://your-image-link.com/english-example.png)
> Screenshot of **SnapExtract**

### 📸 Example 2
![English Text Extraction](https://drive.google.com/file/d/1FBk28iFM67wQ6ILUE6vI6LOb0bn0GzKm/view?usp=sharing)
> Screenshot of **SnapExtract**

### 📸 Example 3
![English Text Extraction](https://drive.google.com/file/d/1MxH3HaIfQCndte31laNeAP9GKUA0Rith/view?usp=sharing)
> Screenshot of **SnapExtract**

![Hindi Text Extraction](https://drive.google.com/file/d/1eC1oOPSDzd5j1w-5tI4CpZcElK-KocZc/view?usp=sharing)
> Screenshot of **SnapExtract**

### 📸 Example 4
![Keyword Search](https://drive.google.com/file/d/1XF4yNPA5r2QdUSyY3xT0TtgkgH-WzhPB/view?usp=sharing)
> Screenshot of **SnapExtract**

### 📸 Example 5
![English Text Extraction](https://drive.google.com/file/d/1dncUTmI9NjST_nJ3PLV1ONCXfZhplbCC/view?usp=sharing)
> Screenshot of **SnapExtract**

You can upload your own results and test the application using various types of images in the **Live Web Application**!

---

## 📌 Additional Notes:
- **Memory Optimization**: To ensure smooth performance and prevent excessive memory consumption, the image processing is efficiently handled by converting the images to smaller numpy arrays and leveraging memory-efficient methods.
- **No Need to Reprocess Images**: Once the text is extracted, only the extracted text is searched when a keyword is entered, avoiding reprocessing the image.

---

## 💡 Future Enhancements:
- **Multi-format Text Output**: Adding options to download the extracted text in **PDF**, **TXT**, or **JSON** format.
- **Customizable Languages**: Extend OCR support for additional languages.
- **Image Preprocessing**: Add features like image enhancement to improve OCR accuracy on poor-quality images.

---

## ❤️ Made with Love
This project is **crafted with passion** by **Parshav Singla**! 🧡
