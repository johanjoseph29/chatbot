import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="your api")

# Create the model configuration
generation_config = {
    "temperature": 1,  # Adjusted to a typical range (0.0 - 1.0)
    "top_p": 1,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Instantiate the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start the chat session
chat_session = model.start_chat(
    history=[]
)

# Main loop for chatting
while True:
    user = input('You: ')
    if user.lower() in ['exit', 'quit']:
        print('Exiting chat')
        break

    r = chat_session.send_message(user)
    print(f"Bot: {r.text}")

