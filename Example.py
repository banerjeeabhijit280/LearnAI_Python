# #This code gets the api key from the os. We load the api key manually.

from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read Gemini API key
API_KEY = os.getenv("GENAI_API_KEY")

if not API_KEY:
    print("Gemini API key not found. Check your .env file.")
    exit(1)

# Create Gemini client
client = genai.Client(api_key=API_KEY)

print("Gemini chatbot ready. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        print("Bye 👋")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    print("Gemini:", response.text)
