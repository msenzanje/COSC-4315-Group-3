import os
from langchain_ollama import OllamaEmbeddings, ChatOllama

class Models:
    def __init__(self):
        self.embeddings_ollama = OllamaEmbeddings(
            model = 'snowflake-arctic-embed:22m',
            prompt = "The sky is blue"
        )

        self.model_ollama = ChatOllama(
            model =  'llama2:latest'
        )
            