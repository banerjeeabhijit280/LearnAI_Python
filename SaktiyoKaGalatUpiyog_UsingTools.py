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
# chat = client.chats.create(
#     model="gemini-2.5-flash",
#     config={
#         "system_instruction": """
# You are a function calling assistant.

# Available functions:
# - add(a, b)
# - subtract(a, b)

# Rules:
# - Always return JSON only

# Example:
# {
#   "function": "add",
#   "arguments": {"a": 5, "b": 3}
# }

# If not related:
# {
#   "function": "none",
#   "message": "I can only do addition and subtraction."
# }
# """
#     }
# )


tools = [
    {
        "function_declarations": [
            {
                "name": "add",
                "description": "Add two numbers",
                "parameters": {
                    "type": "OBJECT",
                    "properties": {
                        "a": {"type": "NUMBER"},
                        "b": {"type": "NUMBER"}
                    },
                    "required": ["a", "b"]
                }
            },
            {
                "name": "subtract",
                "description": "Subtract two numbers",
                "parameters": {
                    "type": "OBJECT",
                    "properties": {
                        "a": {"type": "NUMBER"},
                        "b": {"type": "NUMBER"}
                    },
                    "required": ["a", "b"]
                }
            }
        ]
    }
]


# ask question
chatMsg = input("Ask a math question: ")
# response = chat.send_message(chatMsg)
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="What is 10 minus 4?",
    config={
        "tools": tools
    }
)

if response.candidates[0].content.parts[0].function_call:
    func_call = response.candidates[0].content.parts[0].function_call
    name = func_call.name
    args = func_call.args
    print(name, args)

functions = {
    "add": add,
    "subtract": subtract
}
result = functions[name](**args)



# ai_text = response.text.strip()
# print("AI says:", ai_text)

# ai_text = ai_text.replace("```json", "").replace("```", "").strip()
# # convert JSON string → python dict
# data = json.loads(ai_text)

# # call function
# if data["function"] in functions:
#     args = data["arguments"]
#     result = functions[data["function"]](**args)
#     print("Result:", result)

# elif data["function"] == "none":
#     print(data["message"])


## solution = result, rationale , limitaions