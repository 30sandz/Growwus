import openai

# Set up your OpenAI API key
openai.api_key = 'your-api-key'

# Set the OpenAI engine
engine = "text-davinci-003"

# Infinite loop for taking input
while True:
    # Get user prompt
    prompt = input("Enter your prompt (type 'exit' to quit): ")

    # Check if the user wants to exit
    if prompt.lower() == 'exit':
        break

    # Call the completion endpoint to generate text
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=50
    )

    # Get the generated text from the response
    generated_text = response.choices[0].text.strip()

    # Print the prompt and generated text
    print("\nPrompt:")
    print(prompt)
    print("\nGenerated Text:")
    print(generated_text)
