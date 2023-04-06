import openai
import streamlit as st
from streamlit_chat import message
import os
import requests
import json

openai.api_key = "9685998b101f449ab07c3e6b19b9050e"
openai.api_base =  "https://karshgpt-scus.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = '2022-12-01' # this may change in the future

deployment_name='Karsh-Curie-Test'

@st.cache_data()
def generate_response(user_input, chat_history):
    try:
        prompt = f"{user_input}\n"
        for i in range(max(0, len(chat_history) - 5), len(chat_history)):
            prompt += f"{chat_history[i]['user']}\n{chat_history[i]['bot']}\n"

        completions = openai.Completion.create(
            engine = deployment_name,
            prompt = prompt,
            max_tokens = 100,
            n = 1,
            stop = None,
            temperature = 0.1,
            top_p = 0.3
        )

        if completions.choices:
            message = completions.choices[0].text
            return message.strip()
        else:
            return None
    except Exception as e:
        st.error("Error generating response: " + str(e))
        return None

def get_text():
    input_text = st.text_input("You: ","", key="input")
    return input_text

st.title("KarshGPT")

# Create a session state object to store chat history
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Add a "Reset Chat" button to clear the chat history
if st.button("Reset Chat"):
    st.session_state['history'] = []

user_input = get_text() 

if user_input:
    output = generate_response(user_input, st.session_state['history'])
    if output:
        # Add the current user input and bot response to the chat history
        st.session_state['history'].append({'user': user_input, 'bot': output})

# Display chat history
if 'history' in st.session_state:
    for i in range(len(st.session_state['history'])-1, -1, -1):
        message(st.session_state["history"][i]['bot'], key=str(i))
        message(st.session_state["history"][i]['user'], is_user=True, key=str(i) + '_user')