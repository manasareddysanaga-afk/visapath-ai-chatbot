VisaPath 🇬🇧
AI-Powered UK Immigration Assistant

Sanitised Project Notice
This is a sanitised version of a project I developed as part of my work at a previous company. Company-specific information, proprietary implementation details, credentials, data, and other sensitive information have been removed or modified.

VisaPath is a full-stack AI assistant designed to help users explore UK immigration and visa information through a simple conversational interface.

The application combines a React/Vite frontend, FastAPI backend, and Ollama for local AI inference, allowing the project to run without requiring a paid external AI API during local development.

Disclaimer: VisaPath provides general informational guidance about UK immigration. It does not provide legal advice and is not a replacement for a qualified immigration adviser or solicitor. Immigration rules can change, so users should verify important or current information using official UK Government guidance.

✨ Features

💬 Conversational UK immigration assistant

🤖 Local AI inference using Ollama

🇬🇧 UK visa information and guidance

🔄 Follow-up questions based on user circumstances

🧠 Simple conversation memory

📱 Responsive chat interface

🔗 Official GOV.UK links for common visa routes

⚡ FastAPI REST API

⚛️ React-based frontend

🔐 CORS-enabled frontend/backend integration

💰 No external AI API costs during local development

🛠️ Technology Stack
Frontend

React

Vite

JavaScript

CSS

HTML

Backend

Python

FastAPI

Uvicorn

Ollama Python library

AI

Ollama

llama3.2:latest

Development Environment

Windows

Node.js

Python

Python virtual environment

Git / GitHub

🏗️ System Architecture
                         VisaPath
                            |
               +------------+------------+
               |                         |
           Frontend                   Backend
          React/Vite                 FastAPI
               |                         |
               |      POST /chat         |
               +------------------------>|
                                         |
                                       Ollama
                                         |
                                   llama3.2:latest
                                         |
                                         v
                                    AI Response
                                         |
               <-------------------------+
               |
          Chat Interface

Request Flow

The user enters a question in the React frontend.

The frontend sends the question to the FastAPI backend.

FastAPI adds the recent conversation context.

The backend sends the messages to the locally running Ollama model.

Ollama generates an AI response.

FastAPI returns the response to the frontend.

React displays the response in the chat interface.

📋 Requirements

Before running VisaPath, install the following:

Python

Python 3.10+ is recommended.

Check your installation:

python --version

Node.js

Node.js 18+ is recommended.

Check your installation:

node --version
npm --version

Ollama

Install Ollama from:

https://ollama.com/

Check the installation:

ollama --version


Example:

ollama version is 0.34.3

🤖 AI Model Setup

VisaPath currently uses:

llama3.2:latest


Download the model using:

ollama pull llama3.2


Check installed models:

ollama list


You should see something similar to:

NAME               SIZE
llama3.2:latest    2.0 GB


Ollama must be running while using the chatbot.

📁 Project Structure

The project is organized into separate frontend and backend applications.

ai-visa-assistant/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .venv/
│
├── frontend/
│   ├── app/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── index.html
│
└── README.md

🚀 Backend Setup

Navigate to the backend directory:

cd backend

Create a Virtual Environment
python -m venv .venv


Activate the environment on Windows:

.venv\Scripts\activate


After activation, your terminal should show:

(.venv)

Install Backend Dependencies

The backend uses:

FastAPI

Uvicorn

Ollama

Install them with:

pip install fastapi uvicorn ollama


Alternatively, use the included requirements.txt:

pip install -r requirements.txt


Example requirements.txt:

fastapi
uvicorn
ollama

▶️ Run the Backend

From the backend directory:

uvicorn main:app --reload


The backend should start at:

http://127.0.0.1:8000


You should see:

Application startup complete.

🔌 Backend API

VisaPath provides several API endpoints.

GET /

Checks that the VisaPath API is running.

Example response:

{
  "service": "visapath-backend",
  "product": "VisaPath",
  "version": "2.0"
}

GET /health

Health check endpoint.

Example response:

{
  "status": "ok"
}

POST /chat

Sends a user question to VisaPath.

Request
{
  "message": "I want to work in the UK. What visa options might I have?"
}

Example Response
{
  "response": "There are several possible routes..."
}

📚 API Documentation

FastAPI automatically provides interactive API documentation.

After starting the backend, open:

http://127.0.0.1:8000/docs


This provides a Swagger interface where the /chat endpoint can be tested directly.

💻 Frontend Setup

Open another terminal and navigate to the frontend directory:

cd frontend


Install the frontend dependencies:

npm install


The frontend is built using:

React

React DOM

Vite

Dependencies are defined in:

frontend/package.json

▶️ Run the Frontend

From the frontend directory:

npm run dev


Vite will provide a local development address, usually:

http://localhost:5173


Open the address in your browser to use VisaPath.

🔗 Frontend → Backend Integration

The frontend communicates with the FastAPI backend using a POST request.

Example:

fetch("http://127.0.0.1:8000/chat", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    message: question
  })
});


The backend processes the question using Ollama and returns:

{
  "response": "..."
}


The frontend then displays the response inside the chat interface.

🤖 Ollama Integration

The backend uses the Ollama Python library.

Import Ollama:

import ollama


The model is called using:

result = ollama.chat(
    model="llama3.2:latest",
    messages=messages,
    options={
        "temperature": 0.2,
        "num_predict": 250
    }
)


The generated response is retrieved using:

response = result["message"]["content"]

🧠 Conversation Memory

VisaPath currently uses simple in-memory conversation history.

The backend stores user and assistant messages in:

conversation = []


Only recent messages are sent to the model to reduce latency and unnecessary context.

For example:

recent_conversation = conversation[-6:]


This allows the assistant to understand the recent conversation while keeping the implementation lightweight.

Conversation history is stored only in application memory and can be lost when the backend restarts.

📝 AI Prompt

VisaPath uses a system prompt to guide the AI model.

The prompt instructs the model to:

Provide UK immigration information

Avoid inventing visa names or requirements

Ask useful follow-up questions

Keep responses concise

Avoid presenting itself as a solicitor

Be careful with changing immigration requirements

Direct users to GOV.UK for current official requirements

The AI is intended to act as an information assistant, not as a replacement for professional immigration advice.

🇬🇧 Current Visa Information Scope

The assistant can discuss topics including:

Skilled Worker visa

Health and Care Worker visa

Global Talent visa

Youth Mobility Scheme

Student visa

UK work opportunities

Sponsorship

General visa eligibility questions

Immigration-related follow-up questions

Visa rules and requirements can change. Users should verify current requirements using official GOV.UK guidance.

🔗 Official UK Government Information

Useful official sources include:

UK Visas and Immigration
https://www.gov.uk/browse/visas-immigration

Skilled Worker visa
https://www.gov.uk/skilled-worker-visa

Health and Care Worker visa
https://www.gov.uk/health-care-worker-visa

The application should not treat a locally generated AI response as the final legal or official authority.

🎨 UI Design

VisaPath uses a simple, professional interface designed around:

Neutral earthy colours

Warm ivory background

Beige message areas

Charcoal text

Muted brown primary buttons

Rounded chat cards

Responsive mobile layout

Clear spacing and typography

The interface is intentionally simple so that the main focus remains on the conversation.

▶️ Running the Complete Application

VisaPath requires Ollama, the backend, and the frontend to be running during local development.

Terminal 1 — Ollama

Make sure the model is installed:

ollama list


Confirm that the following model is available:

llama3.2:latest

Terminal 2 — Backend
cd backend
.venv\Scripts\activate
uvicorn main:app --reload


Backend:

http://127.0.0.1:8000

Terminal 3 — Frontend
cd frontend
npm install
npm run dev


Frontend:

http://localhost:5173

🧪 Testing
Test the Backend

Open:

http://127.0.0.1:8000


Expected response:

{
  "service": "visapath-backend",
  "product": "VisaPath",
  "version": "2.0"
}

Test the Health Endpoint

Open:

http://127.0.0.1:8000/health


Expected response:

{
  "status": "ok"
}

Test the Chat API

Open:

http://127.0.0.1:8000/docs


Find the POST /chat endpoint and send:

{
  "message": "I want to work in the UK."
}


The API should return an AI-generated response.

⚠️ Known Limitations

VisaPath is currently an MVP.

The application does not currently include:

Persistent database storage

User accounts

Authentication

Production deployment

Retrieval-Augmented Generation (RAG)

Automated immigration-rule updates

Dedicated immigration knowledge database

Production-grade conversation storage

AI response streaming

Professional legal advice

The current conversation memory is stored in application memory and can be lost when the backend restarts.

🔮 Future Improvements

Potential future improvements include:

Streaming Ollama responses

Persistent conversation storage

Dedicated immigration knowledge base

Retrieval-Augmented Generation (RAG)

Official GOV.UK source retrieval

Improved visa-route classification

Sponsor and employer search

Structured eligibility questions

User authentication

Production deployment

Automated testing

Improved error handling

🧑‍💻 Development Philosophy

VisaPath was developed incrementally, with the initial goal of demonstrating a complete working AI application using a straightforward architecture:

React
  ↓
FastAPI
  ↓
Ollama
  ↓
Llama 3.2
  ↓
FastAPI
  ↓
React


The architecture allows additional infrastructure and capabilities to be introduced as the application evolves.

📊 Project Status

Status: Working MVP

The frontend and backend are integrated, with local AI inference provided by Ollama and the llama3.2:latest model.

👨‍💻 Project Scope

This project demonstrates experience with:

Full-stack application development

React and Vite

FastAPI REST API development

Local LLM integration

Ollama

Prompt engineering

Conversational AI

Frontend/backend integration

API design

Responsive UI development

Local development environments

Git/GitHub workflows

⚖️ Disclaimer

VisaPath provides general informational guidance about UK immigration.

It does not provide legal advice and does not replace a qualified immigration adviser or solicitor.

Immigration rules and requirements can change. Users should verify important or current information using official UK Government guidance.

Sanitisation Notice: This repository is intended for demonstration and portfolio purposes. Proprietary company information, confidential data, credentials, production configuration, and other sensitive implementation details from the original project have been removed or modified.