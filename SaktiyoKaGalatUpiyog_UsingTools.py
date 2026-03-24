#This code works but there is an issue. The code responds like a function call which gives it a machine feel. So next time, we will try to send the reponse of the function to the AI so 
#that the AI generates a response using the result of the function in the code.
import json
from google import genai
import os
from google.genai import types
from dotenv import load_dotenv

# load API key
load_dotenv()
api_key = os.getenv("GENAI_API_KEY")

client = genai.Client(api_key=api_key)

# simple functions
def add(a, b):
    print("Executing add function")
    return a + b

def subtract(a, b):
    print("Executing subtract function")
    return a - b

# function map
functions = {
    "add": add,
    "subtract": subtract
}

tools = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="add",
                description="Add two numbers",
                parameters={
                    "type": "OBJECT",
                    "properties": {
                        "a": {"type": "NUMBER"},
                        "b": {"type": "NUMBER"}
                    },
                    "required": ["a", "b"]
                }
            ),
            types.FunctionDeclaration(
                name="subtract",
                description="Subtract two numbers",
                parameters={
                    "type": "OBJECT",
                    "properties": {
                        "a": {"type": "NUMBER"},
                        "b": {"type": "NUMBER"}
                    },
                    "required": ["a", "b"]
                }
            )
        ]
    )
]

chatMsg = input("Ask a math question: ")
# response = chat.send_message(chatMsg). # this is for chat-based models, for text-based models, use generate_content
response = client.models.generate_content(  # for text-based models, use generate_content
    model="gemini-2.5-flash",
    contents=chatMsg,
    config={
        "tools": tools
    }
)
first_Part = response.candidates[0].content.parts[0]
if first_Part.function_call:               # AI returns a lot of responses called candidates. .candidate[0] means we are filtering out the first candidate which supposed to be the best in the lot.
    #.content reads the candidate 0's value. .part[0] is considering the first part because sometimes AI responses includes texts or other unwanted values in the end. Overall this filtrs out a function call and rejects everything else.
    func_call = response.candidates[0].content.parts[0].function_call
    print("\nThis is what the func_cal have in it: \n",func_call,"\n")
    name = func_call.name
    print("\nGot the name: ",name,"\n")
    args = func_call.args
    print("\nGot the args: ",args,"\n")
   
    print(name, args)

result = functions[name](**args) #The function is getting called here
print("Result: ", result)