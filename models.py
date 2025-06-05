from langchain_ollama import OllamaEmbeddings, ChatOllama

class Models:
    def __init__(self):
        # Snowflake embedding model, BERT arch
        self.embeddings_ollama = OllamaEmbeddings(
            model = 'snowflake-arctic-embed:22m',
        )

        self.model_llava = ChatOllama(
            model= 'llava:7b'
        )

        self.model_llama2 = ChatOllama(  # Model used for intial testing
            model =  'llama2:latest'
        )
            