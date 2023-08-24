# Import Libraries
import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
import pandas as pd
from pandasai import PandasAI
from pandasai.llm import OpenAI

# API Key retrieval
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create LLM
llm = OpenAI(api_token=OPENAI_API_KEY)
pandas_ai = PandasAI(llm)

st.set_page_config(page_title="Data Analysis Tool", page_icon="🔧")

# Sidebar contents
with st.sidebar:
    st.title('Pandas-AI 🐼')
    st.markdown('''
    ## About
    This app is a data analysis tool created using:
    - ### [Streamlit](https://streamlit.io/)
    - ### [Pandas](https://pandas.pydata.org/docs/)
    - ### [PandasAI](https://github.com/gventuri/pandas-ai)
    - ### [OpenAI LLM model](https://platform.openai.com/docs/models)

    ''')
    add_vertical_space(20)
    st.write('Made with ❤️ by [Jayesh_Ironside](https://github.com/jayeshironside)')

# Front-end and Back-end starts here
st.title("Prompt-driven analysis tool 🔧")

uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))
    st.write("Rows x Column :", df.shape)

    prompt = st.chat_input("Enter your prompt here...")

    # if st.button("Generate"):
    if prompt:
        with st.spinner("Generating you response..."):
            st.write(pandas_ai.run(df, prompt=prompt))
    # else:
    #     st.warning("Please enter a prompt.")