from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
client = OpenAI(api_key=api_key)

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message")
    if message:
        messages.append({"role": "user", "content": message})
        chat = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1.0,
            top_p=0.6,
            n=1,
            stream=True
        )
        reply = chat.choices[0].message["content"]
        messages.append({"role": "assistant", "content": reply})
        return jsonify({"reply": reply})
    else:
        return jsonify({"error": "No message provided."}), 400

if __name__ == "__main__":
    app.run(debug=True)
