# The Legal Law Lenz 🤖

The Legal Law Lenz is a Python-based application that allows you to interact with legal documents, retrieve information from them, and answer questions related to the content of these documents. This project combines various technologies and libraries, such as Streamlit, PyPDF2, Hugging Face Transformers, FAISS, and Langchain, to provide a user-friendly interface for querying and extracting information from legal texts.

## Features
- PDF Translation: Upload PDF documents, and the application can translate them into different languages using the Google Translate API.

- Question Answering: Ask questions about the legal documents you've uploaded and receive context-based answers.

- Document Vectorization: The application converts text documents into vector representations using Hugging Face embeddings and stores them in a database for efficient retrieval.

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
