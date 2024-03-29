# import libraries
import os
import chainlit as cl
from langchain import HuggingFaceHub, PromptTemplate, LLMChain
from langchain.chains import SimpleSequentialChain
import streamlit as st

# setting api key
os.environ['HuggingFaceHub_API_TOKEN'] = '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'

# App framework
st.title('AI Food Recalls Analyser')
prompt = st.text_input('Plug in your prompt here')

# Llms
llm=HuggingFaceHub(repo_id="google/gemma-7b",model_kwargs={"temperature":1})

# Get a response in the screen if there's a prompt
if prompt:
    response = llm(prompt)
    st.write(response)

