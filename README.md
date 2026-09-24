# VisaPath 🇬🇧

### AI-Powered UK Immigration Information Assistant

VisaPath is a full-stack conversational AI application designed to help users explore **UK visa and immigration information** through a simple chat interface.

The application combines a **React/Vite frontend**, **FastAPI backend**, and **Ollama-powered local LLM inference** to provide conversational responses and follow-up guidance.

> **Project Notice**
>
> This repository is a sanitised version of a project originally developed as part of my work at a previous company. Company-specific information, proprietary implementation details, credentials, production configuration, confidential data, and other sensitive information have been removed or modified.

---

## 📌 Overview

VisaPath allows users to ask questions about UK immigration and receive conversational, AI-generated guidance.

The application is designed around a simple workflow:

```text
User
  ↓
React / Vite Frontend
  ↓
FastAPI Backend
  ↓
Conversation Context
  ↓
Ollama
  ↓
Llama 3.2
  ↓
AI-Generated Response
  ↓
React Chat Interface
```

The current version is an **MVP** focused on demonstrating full-stack development, conversational AI integration, API design, and local LLM usage.

---

## ✨ Features

* 💬 Conversational UK immigration chatbot
* 🤖 Local AI inference using Ollama
* 🇬🇧 UK visa and immigration information
* 🔄 Follow-up questions using conversation context
* 🧠 Lightweight in-memory conversation history
* 📱 Responsive chat interface
* 🔗 Links to official GOV.UK guidance
* ⚡ FastAPI REST API
* ⚛️ React/Vite frontend
* 🔐 CORS-enabled frontend/backend communication
* 💰 Local AI inference without external AI API costs during development

---

## 🛠️ Technology Stack

| Layer           | Technology                                   |
| --------------- | -------------------------------------------- |
| Frontend        | React, Vite, JavaScript, CSS                 |
| Backend         | Python, FastAPI, Uvicorn                     |
| AI / LLM        | Ollama, Llama 3.2                            |
| API             | REST                                         |
| Development     | Windows, Python virtual environment, Node.js |
| Version Control | Git / GitHub                                 |

---

## 🏗️ Architecture

VisaPath follows a simple frontend/backend architecture.

```text
                         VisaPath
                            │
              ┌─────────────┴─────────────┐
              │                           │
          Frontend                    Backend
         React/Vite                  FastAPI
              │                           │
              │       POST /chat          │
              └──────────────────────────>│
                                          │
                                      Conversation
                                         Context
                                          │
                                          ▼
                                        Ollama
                                          │
                                          ▼
                                  llama3.2:latest
                                          │
                                          ▼
                                    AI Response
                                          │
              ┌───────────────────────────┘
              │
              ▼
        React Chat Interface
```

### Request Flow

```text
User
 ↓
React Frontend
 ↓
POST /chat
 ↓
FastAPI
 ↓
Conversation History
 ↓
Ollama
 ↓
Llama 3.2
 ↓
Generated Response
 ↓
React UI
```

---

## 🤖 AI Model

VisaPath currently uses:

```text
llama3.2:latest
```

The model runs locally through **Ollama**.

The backend uses the Ollama Python library to provide conversation context to the model and receive the generated response.

### Why Local Inference?

Using Ollama allows the project to run an LLM locally during development without requiring a paid external AI API.

This provides:

* Local development
* No external AI API dependency
* No per-request API costs during development
* Greater control over the model environment

---

## 🧠 Conversation Memory

The current MVP uses **simple in-memory conversation history**.

Recent messages are included when generating a response so that the assistant can maintain context across follow-up questions.

For example:

```text
User:
I want to work in the UK.

Assistant:
There are several possible visa routes...

User:
What if I already have a job offer?

Assistant:
If you have a qualifying job offer, the Skilled Worker route may be relevant...
```

### Current Memory Limitations

Conversation history is not persisted in a database.

As a result:

* Conversations are lost when the backend restarts
* There are no user accounts
* There is no long-term conversation storage

---

## 🇬🇧 Information Scope

VisaPath is designed to provide general information about topics including:

* Skilled Worker visa
* Health and Care Worker visa
* Global Talent visa
* Youth Mobility Scheme
* Student visa
* UK work opportunities
* Sponsorship
* General visa eligibility
* Immigration-related follow-up questions

The application is designed to direct users towards **official UK Government guidance** for current requirements.

---

## 📁 Project Structure

```text
visapath-ai-chatbot/
│
├── backend/
│   ├── main.py
│   └── requirements.txt
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
│   │
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── index.html
│
├── PROJECT_DOCUMENTATION.md
├── README.md
└── .gitignore
```

---

# 🚀 Getting Started

## Prerequisites

Before running VisaPath locally, install:

* Python 3.10+
* Node.js 18+
* Ollama
* Git

---

## 1. Install Ollama

Make sure Ollama is installed and running.

Pull the required model:

```bash
ollama pull llama3.2
```

Verify that the model is available:

```bash
ollama list
```

You should see:

```text
llama3.2:latest
```

---

## 2. Start the Backend

Open a terminal in the project directory:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the backend dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn main:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

---

## 3. Start the Frontend

Open a second terminal:

```bash
cd frontend
```

Install the frontend dependencies:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

The frontend will usually be available at:

```text
http://localhost:5173
```

Open the displayed Vite URL in your browser.

---

# 🔌 API

The FastAPI backend exposes a small REST API.

## `GET /`

Returns basic information about the backend.

### Example Response

```json
{
  "service": "visapath-backend",
  "product": "VisaPath",
  "version": "2.0"
}
```

---

## `GET /health`

Returns the backend health status.

### Example Response

```json
{
  "status": "ok"
}
```

---

## `POST /chat`

Sends a user question to the AI assistant.

### Example Request

```json
{
  "message": "I want to work in the UK. What visa options might I have?"
}
```

### Example Response

```json
{
  "response": "There are several possible routes depending on your circumstances..."
}
```

---

## 📖 API Documentation

FastAPI automatically provides interactive API documentation.

Once the backend is running, open:

```text
http://127.0.0.1:8000/docs
```

The Swagger interface can be used to inspect and test the API endpoints directly.

---

# 🎨 User Interface

The interface is designed to keep the conversational experience simple and focused.

### Design Characteristics

* Warm ivory background
* Neutral earthy colour palette
* Beige message areas
* Charcoal text
* Muted brown buttons
* Rounded chat cards
* Responsive mobile layout
* Clear spacing and typography

The UI prioritises readability and keeps the chat experience as the primary interaction.

---

# ⚠️ Current Limitations

VisaPath is currently a **working MVP**.

The current implementation does not include:

* Persistent database storage
* User accounts
* Authentication
* Production deployment
* RAG knowledge base
* Dedicated immigration knowledge database
* Automated immigration-rule updates
* Persistent conversation storage
* Response streaming
* Automated testing infrastructure

### Information Accuracy

AI-generated responses should not be treated as professional immigration or legal advice.

UK immigration rules and requirements can change. Important information should always be verified against the latest official UK Government guidance.

---

# 🔮 Future Improvements

Potential future development includes:

### AI & Knowledge

* Retrieval-Augmented Generation (RAG)
* Dedicated immigration knowledge base
* Official GOV.UK source retrieval
* Automated source updates
* Improved visa-route classification
* More structured eligibility questions

### Application

* Streaming AI responses
* Persistent conversation storage
* User authentication
* User accounts
* Improved error handling
* Automated testing
* Production deployment

### User Experience

* Structured visa eligibility flows
* Better source citations
* Conversation history
* Improved mobile experience
* Clearer distinction between general information and official requirements

---

# 📚 Additional Documentation

More detailed technical information is available in:

```text
PROJECT_DOCUMENTATION.md
```

This document contains additional information about:

* Application architecture
* Development setup
* API endpoints
* AI prompting
* Conversation memory
* Testing
* Limitations
* Development approach

---

# 📊 Project Status

**Status: Working MVP**

The current version demonstrates an integrated:

```text
React/Vite Frontend
        +
FastAPI Backend
        +
Ollama
        +
Llama 3.2
```

The frontend and backend communicate through a REST API, while the backend uses locally hosted LLM inference to generate conversational responses.

---

# 🧑‍💻 Skills Demonstrated

This project demonstrates practical experience with:

* Full-stack application development
* React
* Vite
* JavaScript
* CSS
* Python
* FastAPI
* REST API development
* Ollama
* Local LLM integration
* Prompt engineering
* Conversational AI
* Frontend/backend integration
* API design
* Responsive UI development
* Python virtual environments
* Git/GitHub workflows

---

# ⚖️ Disclaimer

VisaPath provides general informational guidance about UK immigration.

It does **not** provide legal advice and does not replace a qualified immigration adviser or solicitor.

Immigration rules and requirements can change. Users should verify important or current information using official UK Government guidance.

---

# 🔒 Sanitisation Notice

This repository is intended for **demonstration and portfolio purposes**.

The original project was developed in a previous company environment. Company-specific information, confidential data, credentials, production configuration, proprietary implementation details, and other sensitive information have been removed or modified.

This repository is therefore a **sanitised representation** of the original project and may differ from the original production implementation.

---

# 🚀 Quick Start

For a quick local setup:

```bash
# Clone the repository
git clone <your-repository-url>

# Start Ollama
ollama pull llama3.2

# Backend
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

In another terminal:

```bash
# Frontend
cd frontend
npm install
npm run dev
```

Then open:

```text
http://localhost:5173
```

---

## 📌 Conclusion

VisaPath is a full-stack AI-powered UK immigration information assistant built with **React, FastAPI, and Ollama**.

The project demonstrates practical experience in **AI integration, local LLM inference, REST API development, prompt engineering, frontend/backend integration, and responsive web development**.

While the current implementation is an MVP, its architecture provides a foundation for future capabilities such as **RAG, GOV.UK source retrieval, persistent storage, structured eligibility flows, authentication, automated testing, and production deployment**.
