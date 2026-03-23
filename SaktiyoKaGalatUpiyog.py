import json
from google import genai
import os
from dotenv import load_dotenv

# load API key
load_dotenv()
api_key = os.getenv("GENAI_API_KEY")

client = genai.Client(api_key=api_key)

# simple functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# function map
functions = {
    "add": add,
    "subtract": subtract
}

# create chat
chat = client.chats.create(
    model="gemini-2.5-flash",
    config={
        "system_instruction": """
You are a function calling assistant.

Available functions:
- add(a, b)
- subtract(a, b)

Rules:
- Always return JSON only

Example:
{
  "function": "add",
  "arguments": {"a": 5, "b": 3}
}

If not related:
{
  "function": "none",
  "message": "I can only do addition and subtraction."
}
"""
    }
)

# ask question
chatMsg = input("Ask a math question: ")
response = chat.send_message(chatMsg)

ai_text = response.text.strip()
print("AI says:", ai_text)

ai_text = ai_text.replace("```json", "").replace("```", "").strip()
# convert JSON string → python dict
data = json.loads(ai_text)

# call function
if data["function"] in functions:
    args = data["arguments"]
    result = functions[data["function"]](**args)
    print("Result:", result)

elif data["function"] == "none":
    print(data["message"])


## solution = result, rationale , limitaions