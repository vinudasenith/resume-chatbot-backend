import requests

def get_chatbot_response(prompt: str) -> str:
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",  # Ollama API
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False  # turn off streaming for simple usage
            }
        )

        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response from model")

    except Exception as e:
        return f"Error contacting local model: {str(e)}"
