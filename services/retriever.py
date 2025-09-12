from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings
from constants import EMBED_MODEL_NAME

embedding_model =CohereEmbeddings(model =EMBED_MODEL_NAME)
def load_retriver(k=3, save_dir="models/vectorstore"):
    try:
        vectorstore = FAISS.load_local(save_dir, embedding_model, allow_dangerous_deserialization=True)
        retriever = vectorstore.as_retriever(search_kwargs={"k": k})
        return retriever

    except Exception as e:
        print(f"Error occurred at creating retriever side: {repr(e)}")
