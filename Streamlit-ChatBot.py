import openai
import streamlit as st
from streamlit_chat import message

openai.api_key = "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"

@st.cache_data()
def generate_response(user_input, chat_history):
    prompt = f"{user_input}\n"
    for i in range(len(chat_history)):
        prompt += f"{chat_history[i]['user']}\n{chat_history[i]['bot']}\n"
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 3500,
        n = 1,
        stop = None,
        temperature = 0.7,
    )

    if completions.choices:
        message = completions.choices[0].text
        return message
    else:
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