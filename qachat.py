from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-1.5-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit and input:
    response=get_gemini_response(input)
    # Add user query to chat history
    st.session_state['chat_history'].append(("You", input))
    
    # Display streamed response while collecting full response
    st.subheader("The Response is")
    full_response = ""
    response_container = st.empty()
    
    for chunk in response:
        full_response += chunk.text
        response_container.write(full_response)
    
    # Add complete bot response to chat history
    st.session_state['chat_history'].append(("Bot", full_response))

st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")





