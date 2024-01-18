# The Legal Law Lenz 🤖

The Legal Law Lens is a Python-based application that empowers legal professionals to interact with legal documents efficiently. It incorporates various technologies and libraries such as Streamlit, PyPDF2, Hugging Face Transformers, FAISS, Langchain, and OCR capabilities. The project's core features include PDF/TXT translation, question answering, and document vectorization.


## Features

#### 1. PDF/TXT Translation
- Upload PDF or Text documents and translate them into different languages using the Google Translate API.

#### 2. Question Answering
- Ask questions related to the uploaded legal documents and receive context-based answers.

#### 3. Document Vectorization
- Convert pdf/text documents into vector representations using Hugging Face embeddings and store them in a database for efficient retrieval.

#### 4. OCR Integration
- Capture pages from a live camera feed, save them, and perform Optical Character Recognition (OCR) to extract text content.

## Folder Structure

- **model.py:** Main file to run the chatbot/QA system. Execute this file to launch the primary functionality of the Legal Law Lens.

- **ocr.py:** Contains code to run a live camera feed and perform Optical Character Recognition (OCR). This script captures pages, saves them, and extracts text content.

- **translate.py:** Code responsible for translating input PDFs/TXT files into the English language. This functionality is accessible through the Translate Streamlit GUI.

- **vector_store:** Folder storing vector representations of PDF and TXT files. These embeddings facilitate efficient document retrieval.

- **input_pdfs:** Directory containing input PDFs/TXT files. Users can upload legal documents to be processed by the application.

- **translated_pdfs:** Directory storing translated PDFs of the input documents. Translation is performed using the Translate Streamlit GUI.


## Dependencies
- Streamlit
- PyPDF2
- Googletrans
- Transformers
- faiss_cpu
- Langchain
- Ctransformers
- sentence_transformers
- typing-inspect==0.8.0
- typing_extensions==4.5.0
- tkinter
- pytesseract
- OpenCV
