import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Set environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Create the prompt template with a list of dictionaries
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit app interface
st.set_page_config(page_title="Langchain Demo with OpenAI API", page_icon=":robot_face:", layout="wide")
st.title('Langchain Demo with OpenAI API')
st.subheader('Ask any question and get an intelligent response!')

# Add a decorative image or logo (optional)
st.image('https://path-to-your-image/logo.png', width=200)

input_text = st.text_input("Enter your question:")

# OpenAI LLM 
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    with st.spinner('Generating response...'):
        response = chain.invoke({'question': input_text})
        st.success('Response generated!')
    
    st.markdown("### Your Question")
    st.write(input_text)
    
    st.markdown("### Assistant's Response")
    st.write(response)
else:
    st.info("Enter a question above to get started!")

# Add a footer or additional information
st.markdown("""
    ---
    **Powered by**: [Langchain](https://langchain.com) & [OpenAI](https://openai.com)
    """)
