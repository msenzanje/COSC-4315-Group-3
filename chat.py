from models import Models
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_chroma import Chroma as CDb

# Initialize models
models =  Models()
embeddings  = models.embeddings_ollama
llm = models.model_ollama

# Initialize vector store
vector_store  = CDb(
    collection_name="documents",
    embedding_function=embeddings,
    persist_directory="./db/chroma_langchain_db"  # Vector store location
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Answer qustion based on data provided"),
        ("human", "Use the user input {input} to answer question. Use {contect} to"
        "answer question")
    ]
)