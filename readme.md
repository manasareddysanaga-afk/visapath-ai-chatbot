VisaPath 🇬🇧
AI-Powered UK Immigration Assistant

Sanitised Project Notice

This is a sanitised version of a project I developed as part of my work at a previous company. Company-specific information, proprietary implementation details, credentials, data, production configuration, and other sensitive information have been removed or modified.

VisaPath is a full-stack AI chatbot designed to help users explore UK visa and immigration information through a simple conversational interface.

The application combines a React/Vite frontend, FastAPI backend, and Ollama for local AI inference.

✨ Features

💬 Conversational visa and immigration chatbot

🤖 Local AI inference using Ollama

🇬🇧 UK visa and immigration information

🔄 Follow-up questions based on user circumstances

🧠 Simple conversation memory

📱 Responsive chat interface

🔗 Links to official GOV.UK information

⚡ FastAPI REST API

⚛️ React/Vite frontend

🔐 CORS-enabled frontend/backend integration

💰 Local AI inference without external AI API costs during development

🛠️ Technology Stack
Layer	Technology
Frontend	React, Vite, JavaScript, CSS
Backend	Python, FastAPI, Uvicorn
AI	Ollama, Llama 3.2
API	REST
Development	Windows, Python venv, Node.js, Git/GitHub
🏗️ Architecture
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
User
  ↓
React Frontend
  ↓
FastAPI /chat
  ↓
Conversation Context
  ↓
Ollama
  ↓
Llama 3.2
  ↓
AI Response
  ↓
React Chat Interface

🤖 AI Model

VisaPath uses a locally running Ollama model:

llama3.2:latest


The application uses the Ollama Python library to send the conversation context to the local model and receive the generated response.

🧠 Conversation Memory

The current MVP uses simple in-memory conversation history.

Recent messages are provided to the model to maintain conversational context while keeping the implementation lightweight.

Conversation history is not persisted and can be lost when the backend restarts.

🇬🇧 Information Scope

The assistant can provide general information about topics such as:

Skilled Worker visa

Health and Care Worker visa

Global Talent visa

Youth Mobility Scheme

Student visa

UK work opportunities

Sponsorship

General visa eligibility questions

The application is designed to direct users towards official GOV.UK guidance for current requirements.

💻 Running Locally
Requirements

Python 3.10+

Node.js 18+

Ollama

Git

1. Install the AI Model
ollama pull llama3.2


Verify:

ollama list

2. Start the Backend
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload


Backend:

http://127.0.0.1:8000

3. Start the Frontend

Open another terminal:

cd frontend
npm install
npm run dev


Frontend:

http://localhost:5173


Open the frontend address in your browser.

🔌 API
GET /

Returns basic API information.

GET /health

Returns the backend health status.

POST /chat

Accepts a user question and returns an AI-generated response.

Example request:

{
  "message": "I want to work in the UK. What visa options might I have?"
}


FastAPI provides interactive API documentation at:

http://127.0.0.1:8000/docs

🎨 UI

The interface uses a simple, professional design with:

Warm ivory background

Neutral earthy colours

Beige message areas

Charcoal text

Muted brown buttons

Rounded chat cards

Responsive mobile layout

The design keeps the conversational experience as the primary focus.

⚠️ Current Limitations

This is a working MVP.

Current limitations include:

No persistent database

No user accounts

No authentication

No production deployment

No RAG knowledge base

No automated immigration-rule updates

No persistent conversation storage

No response streaming

AI responses are not professional legal advice

Immigration rules can change, so important information should always be verified against current official UK Government guidance.

🔮 Future Improvements

Potential future improvements include:

Streaming Ollama responses

Persistent conversation storage

Dedicated immigration knowledge base

Retrieval-Augmented Generation (RAG)

Official GOV.UK source retrieval

Improved visa-route classification

Structured eligibility questions

User authentication

Production deployment

Automated testing

Improved error handling

📚 Documentation

For more detailed technical documentation, see:

PROJECT_DOCUMENTATION.md

📊 Project Status

Working MVP

The frontend and backend are integrated, with local AI inference provided by Ollama and the llama3.2:latest model.

🧑‍💻 Project Scope

This project demonstrates experience with:

Full-stack application development

React and Vite

FastAPI REST APIs

Local LLM integration

Ollama

Prompt engineering

Conversational AI

Frontend/backend integration

API design

Responsive UI development

Python virtual environments

Git/GitHub workflows

⚖️ Disclaimer

VisaPath provides general informational guidance about UK immigration.

It does not provide legal advice and does not replace a qualified immigration adviser or solicitor.

Immigration rules and requirements can change. Users should verify important or current information using official UK Government guidance.

Sanitisation Notice: This repository is intended for demonstration and portfolio purposes. Proprietary company information, confidential data, credentials, production configuration, and other sensitive implementation details from the original project have been removed or modified.