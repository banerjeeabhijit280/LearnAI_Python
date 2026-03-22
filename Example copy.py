# #This code gets the api key from the os. We load the api key manually.

from google import genai
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

if not API_KEY:
    print("Gemini API key not found. Check your .env file.")
    exit(1)
client = genai.Client(api_key=API_KEY)




response   = client.models.generate_content(
        model="gemini-2.5-flash",

        contents=[
            {
                "role": "user",
                "parts":[{"text": "Write a line about the sea."}]
            }
            ]
        )

print("Gemini:", response.text)
