from langchain.embeddings import HuggingFaceEmbeddings 
from langchain.vectorstores import FAISS
#from langchain.document_loaders import TextFilesLoader  
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader

DATA_PATH = 'translated_pdfs\AFFAIRE A.txt'
DB_FAISS_PATH = 'vectorstore/db_faiss'

def create_vector_db():

  loader = TextLoader(DATA_PATH, encoding='utf-8')

  try:
    documents = loader.load()
  except FileNotFoundError:
    print("Could not access translated_pdfs folder")

  #documents = loader.load()

  print("Documents loaded")

  text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)

  texts = text_splitter.split_documents(documents)

  embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})

  db = FAISS.from_documents(texts, embeddings)

  db.save_local(DB_FAISS_PATH)

  print("Vector DB created")

if __name__ == "__main__":
   create_vector_db()