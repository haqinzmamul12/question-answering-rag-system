from langchain.prompts import PromptTemplate 
from langchain.schema.runnable import RunnablePassthrough 
from constants import MODEL_NAME
from langchain.schema.output_parser import StrOutputParser
from langchain_cohere.chat_models import ChatCohere 
import os 
import pickle
from dotenv import load_dotenv

load_dotenv()  # Load from .env if present
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if not COHERE_API_KEY:
    raise ValueError("GROQ_API_KEY is missing. Please set it in Render environment variables.")
os.environ["COHERE_API_KEY"] = COHERE_API_KEY


def get_answer(query, retriever):
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


        # llm = ChatCohere(model =MODEL_NAME)  command-a-03-2025
        llm = ChatCohere(model ="command-a-03-2025")  

        rag_chain =(
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt 
            | llm 
            | StrOutputParser() 
        )
        response =rag_chain.invoke(query)
        return response
    
    except Exception as e:
        print(f"Error occured at generator side: {e}")