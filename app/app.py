import streamlit as st  
import tempfile 
import os 
import sys 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from services import pdf_processor, embedder, generator

st.set_page_config(page_title ="PDF Q&A with Langchain + Gemma", layout ="centered")
st.title("Ask Questions from Your PDF")

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore =None 

uploaded_file =st.file_uploader("Upload a PDF file", type =['pdf'])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read()) 
        tmp_path =tmp.name 

    st.success("PDF Uploaded Successfully!") 

    with st.spinner("Processing PDF..."):
        raw_text =pdf_processor.extract_text(tmp_path) 
        documents =pdf_processor.chunk_text(raw_text) 
        vectorstore =embedder.create_vectorstore(documents)

        st.session_state.vectorstore =vectorstore 
    st.success("Document Indexed! Drop your question below.")


query = st.text_input("Type your Question Here!")
if query and st.session_state.vectorstore:
    with st.spinner("Generating answer..."):
        answer =generator.get_answer(query, st.session_state.vectorstore)
        st.markdown("## Answer:")
        st.write(answer)