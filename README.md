# 🧾 Resume Matcher Pro Chatbot Backend

## 🧩 Overview 

This repository contains the backend for the AI-powered chatbot feature of **Resume Matcher Pro**, a web application designed to help users optimize ATS-compatible resumes. Built with **FastAPI**, this backend leverages the **Ollama** Gemma:2b model to provide career coaching and resume improvement suggestions through RESTful APIs. It integrates seamlessly with the main Resume Matcher Pro backend (Java/Spring Boot) and frontend (Angular) via CORS-enabled APIs, enabling real-time user interactions.

## ✨ Features

- **AI-Powered Chatbot**: Delivers concise, conversational career coaching responses (2–3 sentences) for resume improvement and job application queries.
- **RESTful API**: Exposes a `/api/v1/chat` endpoint to handle user messages and return AI-generated responses.
- **Ollama Integration**: Uses the Gemma:2b model running locally for efficient, privacy-focused AI processing.
- **CORS Support**: Configured to allow communication with the Angular frontend at `http://localhost:4200`.
- **Scalable Architecture**: Built with FastAPI for high-performance, asynchronous API handling.

## 🛠️ Tech Stack 

- **Framework**: FastAPI
- **Language**: Python 3.8+
- **AI Model**: Ollama (Gemma:2b)
- **Dependencies**:
  - `fastapi` (RESTful APIs)
  - `pydantic` (Data validation and schemas)
  - `requests` (Ollama API communication)
  - `uvicorn` (ASGI server)
- **Build Tool**: Python (pip for dependency management)

## ⚙️ Prerequisites

Ensure the following are installed before setting up the project:

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Ollama (running locally with the Gemma:2b model at `http://localhost:11434`)
- Access to the [Resume Matcher Pro Backend](https://github.com/vinudasenith/resume-app-backend.git) and [Frontend](https://github.com/vinudasenith/resume-app-frontend.git) for full integration

## 🚀 Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vinudasenith/resume-app-chatbot-backend.git
   cd resume-app-chatbot-backend
   ```

2. **Install Dependencies**:
   - Create a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install required packages from `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Ollama**:
   - Install Ollama and ensure the Gemma:2b model is available.
   - Start the Ollama server:
     ```bash
     ollama run gemma:2b
     ```
   - Verify the server is running at `http://localhost:11434`.

4. **Configure Environment**:
   - The API is pre-configured to connect to Ollama at `http://localhost:11434/api/chat`.
   - CORS is set to allow requests from the frontend at `http://localhost:4200`. Update `app/main.py` if the frontend runs on a different URL:
     ```python
     app.add_middleware(
         CORSMiddleware,
         allow_origins=["http://localhost:4200"],
         allow_credentials=True,
         allow_methods=["*"],
         allow_headers=["*"],
     )
     ```

5. ▶️ **Run the Application** :
   - Start the FastAPI server:
     ```bash
     uvicorn app.main:app --reload --port 8001
     ```
   - The API will be available at `http://localhost:8001`.

## Usage

1. **Interact with the Chatbot**:
   - Send a POST request to `http://localhost:8001/api/v1/chat` with a JSON body:
     ```json
     {
       "message": "How can I improve my resume for a software engineering role?"
     }
     ```
   - The response will contain the AI-generated reply:
     ```json
     {
       "response": "Focus on quantifying your achievements and use keywords from the job description. Ensure your technical skills are clearly listed."
     }
     ```

2. **Integration with Frontend**:
   - The Angular frontend sends user messages to the `/api/v1/chat` endpoint, which this backend processes and responds to with career coaching advice.

##📂  Project Structure 

```plaintext
root-folder/
├── app/
│   ├── __pycache__/            # Python compiled bytecode cache
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           └── chat.py     # Chatbot API endpoint
│   ├── models/                 # Data models (if any)
│   ├── schemas/
│   │   └── chat_schema.py      # Pydantic models for request/response
│   ├── services/
│   │   └── chat_service.py     # Chatbot service logic
│   └── main.py                 # FastAPI application entry
├── .gitignore                  # Files ignored by Git
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 🔗 API Endpoints

- `POST /api/v1/chat`  
  - **Request Body**: `{ "message": "User query" }`  
  - **Response**: `{ "response": "AI-generated reply" }`  
  - **Description**: Processes user input and returns a career coaching response from the Gemma:2b model.

> **Note**: The endpoint is CORS-enabled for the Angular frontend at `http://localhost:4200`.

## 📜 License 

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📧 Contact

For questions, feedback, or issues, contact [ha.vinudas@gmail.com](mailto:ha.vinudas@gmail.com) or open an issue on GitHub.

## Related Repositories

- Frontend repository: https://github.com/vinudasenith/resume-app-frontend.git
- Backend repository: https://github.com/vinudasenith/resume-app-backend.git
- Resume Parser AI repository: https://github.com/vinudasenith/resume-parser-ai.git
