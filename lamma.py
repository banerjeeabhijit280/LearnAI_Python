import requests
import json

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "mistral",
        "prompt": "Explain Spark"#,
        # "stream": False   # 🔥 IMPORTANT
    }
)

# print(response.json()["response"])
for line in response.iter_lines():
    if line:
        data = json.loads(line)
        print(data.get("response", ""), end="", flush=True)