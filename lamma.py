import requests
import json
while True:
    Query = input("\nYou: ")

  
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": Query
            # "prompt": "Explain Spark"T
        }
    )

    # print(response.json()["response"])
    print("Mistral: ")
    for line in response.iter_lines():
        if line:
            data = json.loads(line)
            print(data.get("response", ""), end="", flush=True)f