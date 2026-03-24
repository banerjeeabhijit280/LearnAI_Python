import json
from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GENAI_API_KEY")

client = genai.Client(api_key=api_key)

def add(a, b):
    return a + b

def sub(a,b):
    return a + b

def mul(a, b):
    return a * b


functions = {
    "add": add,
    "subtract": sub,
    "multiply": mul
}
tools: [
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
                "name": "sub",
                "description": "Subtract two numbers",
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
                "name": "mul",
                "description": "Multiply two numbers",
                "Parameters": {
                    "Type": "OBJECT",
                    "properties": {
                        "a" : {"type": "NUMBER"},
                        "b" : {"type": "NUMBER"}
                    }
                }
            }
        ]
    }
] # type: ignore

chatMsg = input("Ask a math question: ")
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
result = functions[name](**args)
