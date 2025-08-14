from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import FAISS 
from app.constants import EMBED_MODEL_NAME

def create_vectorstore(documents):
    try:
        embedding =HuggingFaceBgeEmbeddings(model_name =EMBED_MODEL_NAME)
        vectorstore =FAISS.from_documents(documents= documents, embedding= embedding)
        return vectorstore
    
    except Exception as e:
        print(f"Error at creating vector store: {repr(e)}")