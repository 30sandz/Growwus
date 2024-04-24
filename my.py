import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]


while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages,
            temperature=1.0,
            top_p = 0.6,
            n=1,
            
        )
    
    reply = chat.choices[0].message.content

    print(f"ChatGPT: {reply}")
    print(f"ChatGPT:2 {reply2}")
    messages.append({"role": "assistant", "content": reply})

