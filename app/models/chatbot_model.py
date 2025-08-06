# app/models/chatbot_model.py
import requests

class LocalChatbot:
    def __init__(self, model_name="gemma:2b"):
        self.api_url = "http://localhost:11434/api/chat"
        self.model_name = model_name

    def generate_response(self, prompt: str) -> str:
        try:
            response = requests.post(self.api_url, json={
                "model": self.model_name,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            })

            if response.status_code == 200:
                result = response.json()
                return result['message']['content']
            else:
                return "Error: Model returned status code " + str(response.status_code)
        except Exception as e:
            return f"Error contacting local model: {e}"

# Instantiate chatbot
chatbot = LocalChatbot()
