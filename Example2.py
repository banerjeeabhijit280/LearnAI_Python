#This code loads the api key by itself. This happens because we are using the variable name in the .env file as recomendation by the AI provider (openapi here)
from google import genai
from dotenv import load_dotenv
import os

def get_genai_client():
    load_dotenv()

    api_key = os.getenv("GENAI_API_KEY")
    if not api_key:
        print("Gemini API key not found")
        exit(1)

    return genai.Client(api_key=api_key)

def chat_with_ai(client):
    print("Gemini chatbot ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            break

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

        print("Gemini:", response.text)

# ---- main ----
client = get_genai_client()
chat_with_ai(client)

