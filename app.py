#Dependencias
#for graphical user interface, streamlit; for reading pdf pypdf
#for interacting with llm langchain, python-dotenv for the secrets
#faiss-cpu for vestor storing, huggingface for llm models.
import streamlit as st

def main():
    #main header for the app
    st.set_page_config(page_title="Ask pdf", page_icon=":books:")
    st.header(page_title = "Preguntale a tus PDF :smile:")
    
    #text imput for the user to ask questions
    
    
if __name__== '__main__':
    main()