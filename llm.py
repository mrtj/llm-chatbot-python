import streamlit as st

from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

openai_api_key = st.secrets['OPENAI_API_KEY']
openai_model = st.secrets['OPENAI_MODEL']

embeddings = OpenAIEmbeddings(
    openai_api_key=openai_api_key
)

llm = ChatOpenAI(
    openai_api_key=openai_api_key,
    model=openai_model,
    verbose=True,
)
