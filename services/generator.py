from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate 
from langchain.schema.runnable import RunnablePassthrough 
from config import GROQ_API_KEY 
from constants import GEMMA_MODEL_NAME
from services.retriever import get_retriever
from langchain.schema.output_parser import StrOutputParser 
import os 

os.environ["GROQ_API_KEY"] =GROQ_API_KEY 

def get_answer(query, vectorstore):
    try:
        template ="""
        You are an AI assistant and you have been tasked to answer the user query based on the following context.
        A context will be provided to you from retriever and based on this you have to generate response for user's question.
        If you don't get context then say 'Sorry!, I did not received enough context to answer your query.'.

        question:{question}
        context:{context}
        """
        prompt =PromptTemplate(
            template =template,
            input_variables= ["context", "question"]
        )

        retriever =get_retriever(vectorstore)
        llm =ChatGroq(model_name =GEMMA_MODEL_NAME)

        rag_chain =(
            {"Context": retriever, "question": RunnablePassthrough()}
            | prompt 
            | llm 
            | StrOutputParser() 
        )
        response =rag_chain.invoke(query)
        return response 
    
    except Exception as e:
        print(f"Error occured at generator side: {repr(e)}")