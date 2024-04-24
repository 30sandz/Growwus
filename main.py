import requests

URL = "https://api.openai.com/v1/chat/completions"

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

payload = {
"model": "gpt-3.5-turbo",
"messages": [{"role": "user", "content": f"What is the first computer in the world?"}],
"temperature" : 1.0,
"top_p":1.0,
"n" : 1,
"stream": False,
"presence_penalty":0,
"frequency_penalty":0,
}

headers = {
"Content-Type": "application/json",
"Authorization": "API_KEY"
}

response = requests.post(URL, headers=headers, json=payload, stream=False)
     

response.content