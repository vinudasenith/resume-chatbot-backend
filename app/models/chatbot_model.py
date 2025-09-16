import requests

class LocalChatbot:
    def __init__(self, model_name="gemma:2b"):
        self.api_url = "http://localhost:11434/api/chat"
        self.model_name = model_name


    # Function to generate a response
    def generate_response(self, prompt: str) -> str:
        try:
            response = requests.post(self.api_url, json={
                "model": self.model_name,
                "messages":[ 
                    {"role": "system", "content": "You are a career coach. Answer in 2–3 short sentences. Be direct and conversational. Do NOT give long lists unless the user explicitly asks for step-by-step details."},
                    {"role": "user", "content": prompt}
                    ],
                "stream": False, 
            })

            if response.status_code == 200:
                data = response.json()
                return data.get("response", "No response from model")
            else:

                return f"Error: Model returned status code(response.status_code)"
        except Exception as e:
            return f"Error contacting local model: {e}"


# Instantiate chatbot
chatbot = LocalChatbot()
