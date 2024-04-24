# Importing necessary libraries
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Loading environment variables from .env file
load_dotenv()

# Retrieving API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initializing OpenAI client with API key
client = OpenAI(api_key=api_key)

# Initializing conversation messages with a system message
messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

# Defining the main function to run the Streamlit app
def main():
    # Setting page title
    st.title("Growwus")

    # Displaying introduction text
    st.write("Welcome to the Growwus conversation!")

    # Text input field for user to enter messages
    user_input = st.text_input("User:")
    st.write(user_input)

    # Checking if user has entered a message
    if user_input:
        
        # Appending user's message to conversation history
        messages.append({"role": "user", "content": user_input})

        # Generating AI assistant's reply
        chat = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1.0,
            top_p=0.6,
            n=1,
        )

        # Extracting reply from chat
        reply = chat.choices[0].message.content

        # Displaying AI assistant's reply
        st.text_area("ChatGPT:", value=reply, height=200)
        st.write(reply)

        # Appending AI assistant's reply to conversation history
        messages.append({"role": "assistant", "content": reply})

# Running the Streamlit app
if __name__ == "__main__":
    main()