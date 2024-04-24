from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

api_key = 'sk-proj-FlmUvRw2jhvFApKi79mVT3BlbkFJI1TFLa2exEJlF8th83s4'

client = OpenAI(api_key=api_key)

messages = [
    {"role": "assistant", "content": "You are a kind helpful assistant."},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    if user_input : 
        # Format user input as a message
        user_message = {"role": "user", "content": user_input}
        # Append user message to messages array
        messages.append(user_message)

        # Call OpenAI API with messages array
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,  # Pass the messages array
            max_tokens=1,
            temperature=0.6,
            top_p=0.6,
            n=1,
        )

        # Get the response message from the API
        response_text = response.choices[0].message.content

        # Append AI response to messages array
        ai_message = {"role": "system", "content": response_text}
        messages.append(ai_message)

    # Render the response in the chat interface
    return render_template('index.html',messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
