import os
import time
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma  import Chroma 
from models import Models
from uuid import uuid4

# Initialize the models
models = Models()
embeddings  = models.embeddings_ollama
llm = models.model_ollama

# Define cnstants
exam_foler = "/.Exam Collection"
chunk_size = 1000
chunk_overlap = 50
chunk_interval =  10

# Chroma vector store
vector_store = Chroma(
    collection_name="documents",
    embedding_function=embeddings,
    # Storing vector space locally
    persist_directory="./db/chroma_langchain_db",
)


