import os
import openai
import toml


secrets_file = os.path.join(os.path.dirname(__file__), 'secrets.toml')
secrets = toml.load(secrets_file)

openai_api_key = secrets['chatgpt']['api_key']
openai.api_key = openai_api_key

messages = [
 {"role": "system", "content" : ""}
]

while True:
    content = input("User: ")
    messages.append({"role": "user", "content": content})
    
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    messages.append({"role": "assistant", "content": chat_response})