# Use a base image with Python
FROM python:3.12-slim

# Install Tesseract and other dependencies
RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your Streamlit app code
COPY . .

# Install required Python packages
RUN pip install -r requirements.txt

# Command to run the app
CMD ["streamlit", "run", "app.py"]
