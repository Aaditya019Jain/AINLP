import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["langchain_api_key"] = os.getenv("langchain_api_key")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please help me with the following task."),
        ("user","Question:{question}"),
    ]
)

st.title("Langchain Chatbot with LLama")
input = st.text_input("Enter your message...")

llm = Ollama(model="phi")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input:
    st.write(chain.invoke({'question': input}))


