from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os 
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load gemini 

model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_reponse(question):
    response=chat.send_message(question,stream=True)
    return response

st.header("Gemini Chatbot")


#intialization of ssssion state for chat history if it doesnt exist 
if "chat_history" not in st.session_state:
    st.session_state.session_state["chat_history"]=[]


input=st.text_input("Input: ",key="input")
submit=st.button("Ask your question")

if submit and input:
    response=get_gemini_reponse(input)

    ##add user query and response to chat history 
    st.session_state.chat_history.append({"You":input,"gemini":response})
    st.subheader("Gemini's Response:")

    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('bot', chunk.text))

st.subheader("Chat History")

for role,text in st.session_state['chat_history']:
    if role=="You":
        st.write(f"**You:** {text}")
    else:
        st.write(f"**Gemini:** {text}")