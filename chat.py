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

# Template used to guide esponse
prompt = ChatPromptTemplate.from_messages(
    [
     ("system", "You are a student taking an exam. Answer each\
       question thoroughly and completely."),
     ("human", "Using the provided input: {input}, and the \
        context: {context}, answer all questions. Make sure you \
        respond to every part of the prompt.")
    ]
)

# Define the retrieval chain
# Retriver from our vector store. To find and retrieve relevent docs
retriever = vector_store.as_retriever(kwargs={"k":10}) # 10 most relevant docs
combine_docs_chain = create_stuff_documents_chain(
    llm, prompt
)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

# No vector use
chain = prompt | llm


# Main loop
def chatbot(query:str)->str:
    result = chain.invoke({"input": query, "context": None})
    
    return(f'{result}')