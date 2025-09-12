import os 
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS 
from langchain_cohere import CohereEmbeddings
from constants import EMBED_MODEL_NAME

load_dotenv() 
COHERE_API_KEY =os.getenv("COHERE_API_KEY")
os.environ['COHERE_API_KEY'] =COHERE_API_KEY

def create_vectorstore(documents, save_dir ="models/vectorstore"):
    try:
        embedding =CohereEmbeddings(model =EMBED_MODEL_NAME)
        vectorstore =FAISS.from_documents(documents= documents, embedding= embedding)

        os.makedirs(save_dir, exist_ok=True)
        vectorstore.save_local(save_dir)
        print(f"Vectorstore saved to {save_dir}")
    
    except Exception as e:
        print(f"Error at creating vector store: {repr(e)}")