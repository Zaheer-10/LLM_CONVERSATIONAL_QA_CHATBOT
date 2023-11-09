import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

load_dotenv()


st.set_page_config(page_title="Conversational Q&A ChatBot 🤖")

st.sidebar.markdown("### Instructions")
st.sidebar.info(
    "1. Type your question in the left column.\n"
    "2. Click 'Ask your Query' to get a response from the ChatBot.\n"
    "3. Explore the ChatBot's answers and have a conversation!\n"
    "4. Feel free to ask anything. The ChatBot is here to help!"
)
st.image("conv_chatbot.jpg", use_column_width=True)


chat = ChatOpenAI(temperature=0.5)

if 'getmessage' not in  st.session_state:
    st.session_state['getmessage'] = [SystemMessage(content='Your are a comedian AI assistant')]
    
def Get_ChatBot_Response(query):
    st.session_state['getmessage'].append(HumanMessage(content=query))
    answer = chat(st.session_state['getmessage'])
    st.session_state['getmessage'].append(AIMessage(content=answer.content))
    return answer.content


st.write("### Ask Questions")
user_input = st.text_input('Type your query:', key='input_')

if st.button("Submit"):
    st.subheader("Generated response is 🚀\n")
    response = Get_ChatBot_Response(user_input)
    st.write(response)

