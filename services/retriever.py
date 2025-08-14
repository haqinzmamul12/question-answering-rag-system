def get_retriever(vectorstore, k =3):
    try:
        retriever =vectorstore.as_retriever(search_kwargs ={"k":k})
        return retriever 
    except Exception as e:
        print(f"Error occured at creating retriever side: {repr(e)}")