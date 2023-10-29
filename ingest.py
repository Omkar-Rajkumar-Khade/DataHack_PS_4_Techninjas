from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.document_loaders import TextLoader

DATA_PATH = 'translated_pdfs'
DB_FAISS_PATH = 'vectorstore/db_faiss'

import chardet

# Create vector database
def create_vector_db():
    loader = DirectoryLoader('./translated_pdfs', glob="**/*.txt", loader_cls=TextLoader)

    documents = []
    for document in loader.load():
        try:
            with open(document.filepath, 'rb') as file:
                rawdata = file.read()
                result = chardet.detect(rawdata)
                file_encoding = result['encoding']
                text = rawdata.decode(file_encoding)
                document.text = text
                documents.append(document)
        except Exception as e:
            print(f"Error loading {document.filepath}: {e}")

    print("Documents loaded successfully")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    texts = text_splitter.split_documents(documents)
    print("Text splitting done successfully")

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
    print("Embeddings model loaded successfully")

    db = FAISS.from_documents(texts, embeddings)
    db.save_local(DB_FAISS_PATH)
    print("Databases saved successfully")

if __name__ == "__main__":
    create_vector_db()

