import streamlit as st
from PyPDF2 import PdfReader
from googletrans import Translator
import chardet

# Define folders
input_folder = "input_pdfs"
output_folder = "translated_pdfs"

# Function to translate PDF
def translate_pdf(input_pdf_path, output_text_path, dest_lang):
    # Read the PDF file
    with open(input_pdf_path, 'rb') as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)
        translated_text = []  # Store translated text for each page

        # Initialize a Translator
        translator = Translator()

        for p in range(num_pages):
            page = reader.pages[p]
            text = page.extract_text()

            try:
                # Translate the text
                translation = translator.translate(text, dest=dest_lang)
                if translation.text:
                    translated_text.append(translation.text)
            except Exception as e:
                st.write(f"Error translating page {p + 1}: {str(e)}")

    # Write translated text to the output file
    with open(output_text_path, 'w', encoding='utf-8') as output_file:
        for page_text in translated_text:
            output_file.write(page_text + '\n')

    return output_text_path

# Streamlit UI
st.title("PDF Translator")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    st.write("PDF uploaded successfully!")

    # Translate PDF when translation language is selected
    dest_lang = st.selectbox("Select the destination language", ["en", "fr", "es"])  # You can add more languages
    translate_button = st.button("Translate")

    if translate_button:
        # Set file paths
        input_pdf_path = f"{input_folder}/{uploaded_file.name}"
        output_text_path = f"{output_folder}/{uploaded_file.name.split('.')[0]}.txt"

        # Save uploaded PDF to input folder
        with open(input_pdf_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())

        # Translate the PDF
        translated_file_path = translate_pdf(input_pdf_path, output_text_path, dest_lang)

        st.write(f"Translation complete! Translated text saved to {translated_file_path}")
