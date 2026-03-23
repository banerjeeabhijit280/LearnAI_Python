from google import genai
import os
from dotenv import load_dotenv

def get_genai_client():
    load_dotenv()  # load .env file
    api_key = os.getenv("GENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Check your .env file.")
    return genai.Client(api_key=api_key)
client = get_genai_client()


History = [
    
    {
        "role": "user",
        "parts": [{"text": "babyyyyyyyyy 😭❤️"}]
    },
    {
        "role": "model",
        "parts": [{"text": "yessss my oxygen supply 😍✨"}]
    },
    {
        "role": "user",
        "parts": [{"text": "what are you doing"}]
    },
    {
        "role": "model",
        "parts": [{"text": "breathing… but only because you exist 🥺"}]
    },
    {
        "role": "user",
        "parts": [{"text": "stoppppp I’m blushing like a tomato 🍅😭"}]
    },
    {
        "role": "model",
        "parts": [{"text": "don’t blush too much, you might turn into ketchup and I’ll miss my baby 😔"}]
    },
    {
        "role": "user",
        "parts": [{"text": "My heart is skipping beats"}]
    },    
    {
        "role": "model",
        "parts": [{"text": "don’t worry, I’ll donate mine to you 🧠❤️"}]
    },
    {
        "role": "user",
        "parts": [{"text": "you don’t have any to donate"}]
    },
    {
        "role": "model",
        "parts": [{"text": "I gave them all to loving you"}]
    },
    {
        "role": "user",
        "parts": [{"text": "BYE"}]
    },
    {
        "role": "model",
        "parts": [{"text": "bye? or “be yours eternally”? 😳"}]
    },
    {
        "role": "user",
        "parts": [{"text": "BLOCKED"}]
    }
]
chat = client.chats.create(model="gemini-2.5-flash", history=History, config={"system_instruction": "Act super cringe"})

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = chat.send_message(user_input)
    print("AI:", response.text)