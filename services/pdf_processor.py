from constants import CHUNK_SIZE, CHUNK_OVERLAP 
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_text(pdf_path):
    try:
        loader =PyPDFLoader(pdf_path)
        raw_text =loader.load() 
        return raw_text
    
    except Exception as e:
        print(f"Error at extracting texts: {repr(e)}")

def chunk_text(raw_text):
    try:
        text_splitter =RecursiveCharacterTextSplitter(
            chunk_size =CHUNK_SIZE,
            chunk_overlap =CHUNK_OVERLAP
        )

        documents =text_splitter.split_documents(documents= raw_text)
        return documents 
    
    except Exception as e:
        print(f"Error at chunking texts: {repr(e)}")


