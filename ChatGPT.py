import os
import openai
openai.api_key = "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"

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