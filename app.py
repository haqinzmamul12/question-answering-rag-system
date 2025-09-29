import streamlit as st  
import tempfile 

from services import pdf_processor, embedder, generator, retriever

st.set_page_config(page_title="PDF Q&A with Langchain + Gemma", layout="centered")
st.title("Ask Questions from Your PDF")

# Init session state keys
if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

uploaded_file = st.file_uploader("Upload a PDF file", type=['pdf'])

if uploaded_file and not st.session_state.pdf_processed:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read()) 
        tmp_path = tmp.name 

    st.success("PDF Uploaded Successfully!") 

    with st.spinner("Processing PDF..."):
        raw_text = pdf_processor.extract_text(tmp_path) 
        documents = pdf_processor.chunk_text(raw_text) 
        embedder.create_vectorstore(documents)
        retr = retriever.load_retriver()

        st.session_state.retriever = retr 
        st.session_state.pdf_processed = True   # ✅ prevent re-processing
    st.success("Document Indexed! Drop your question below.")

# Input box & QnA
query = st.text_input("Type your Question Here!")
if query and st.session_state.retriever:
    with st.spinner("Generating answer..."):
        answer = generator.get_answer(query, st.session_state.retriever)
        st.markdown("## Answer:")
        st.write(answer)

# Website URL: https://retrieval-information-system.onrender.com/ 