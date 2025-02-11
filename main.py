# import all the required libraries
import vertexai
import streamlit as st
import os
from vertexai.preview.generative_models import (
    # functions to create the model
    GenerationConfig,
    GenerativeModel
)

from dotenv import load_dotenv

load_dotenv()

project_id=os.getenv("project_id")
project_region=os.getenv("region")

# authentication with vertextai
vertexai.init(project=project_id,location=project_region)

# Load the model
model=GenerativeModel("gemini-1.0-pro")


def user_interfaces():
    st.set_page_config("VertextAI")
    st.header("VertexAI Local Setup")

    user_question=st.text_input("Ask me anything...")

    if user_question:
        response=model.generate_content(user_question,stream=True)


        for res in response:
            st.write(res.text,end="")


## Call the function
if __name__=="__main__":
    user_interfaces()