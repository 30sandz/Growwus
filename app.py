from flask import Flask, render_template, request
from openai import OpenAI
import random

api_key = "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"

app = Flask(__name__)

client = OpenAI(api_key=api_key)

messages = [
    {"role": "assistant", "content": "You are a kind helpful assistant"},
]

@app.route('/')
def home():
    num = random.randint(1000,9999)
    return render_template('index.html', num=num)

@app.route('/ask/<int:num>', methods=['POST','GET'])
def ask(num):
    user_input = request.form['user_input']
    if user_input : 

        user_message = {"role": "user", "content": user_input}

        messages.append(user_message)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=2000,
            temperature=0.7,
            n=1,
        )

        response_text = response.choices[0].message.content


        ai_message = {"role": "system", "content": response_text}
        messages.append(ai_message)


    return render_template('index.html',messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
