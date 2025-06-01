# Load the required packages
import streamlit as st
from groq import Groq

# Intialize the streamlit app
st.set_page_config(page_title="GEN AI Project")

# LOad the API key
api_key = st.secrets["GROQ_API_KEY"]

# Initialize the groq api
client = Groq(api_key=api_key)

# Function to generate response from the model
def get_response(text:str,model_name="llama-3.3-70b-versatile"):
    stream = client.chat.completions.create(
        messages = [
        {
            "role":"system",
            "content":"You are a helpful assistant"
        },
        {
            "role":"user",
            "content":text
        }
        ],
        model =model_name,
        stream = True
    )

    for chunk in stream:
        response = chunk.choices[0].delta.content
        if response is not None:
            yield response
# Add the title to streamlit app
st.title("LLama 3.3 Model")
st.subheader("by Sindhura Nadendla")

# Provide text area input for user
user_input = st.text_area("Ask your question: ")

# Create submit button
submit = st.button("Generate",type="primary")

# IF button is clicked
if submit:
    st.subheader("Model Response")
    st.write_stream(get_response(user_input))
