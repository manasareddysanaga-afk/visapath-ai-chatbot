# VisaPath

## AI-Powered UK Immigration Information Assistant

VisaPath is a full-stack AI application designed to help users explore UK immigration and visa information through a simple conversational interface.

The application combines a **React/Vite frontend**, **FastAPI backend**, **LangChain**, **Chroma vector database**, and **Ollama/Llama 3.2** for local AI inference.

VisaPath uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant GOV.UK reference information before generating an answer. The system also includes **Langfuse observability**, **hallucination controls**, **faithfulness evaluation**, and an automated **20-question RAG evaluation suite**.

The project is designed as a portfolio/development project demonstrating practical experience with full-stack development, local LLM integration, RAG pipelines, prompt engineering, evaluation, and LLM observability.

---

## ⚠️ Disclaimer

VisaPath provides general informational guidance about UK immigration.

It does **not** provide legal advice and is not a replacement for a qualified immigration adviser or solicitor.

UK immigration rules can change. Users should verify important or current information using official UK Government guidance before making immigration decisions.

---

## 🔐 Sanitised Project Notice

This repository is a sanitised version of a project developed for demonstration and portfolio purposes.

Company-specific information, proprietary implementation details, credentials, confidential data, production configuration, and other sensitive information have been removed or modified.

No private company credentials or proprietary production information should be included in this repository.

---

# ✨ Features

VisaPath currently provides:

- 💬 Conversational UK immigration assistant
- 🇬🇧 UK visa information and guidance
- 🤖 Local LLM inference using Ollama
- 🦙 Llama 3.2
- 🔗 LangChain integration
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 GOV.UK reference document retrieval
- 🗄️ Chroma vector database
- 🔎 Semantic similarity search
- 🛡️ Hallucination/grounding controls
- 📊 Langfuse tracing and observability
- 🎯 Faithfulness evaluation
- 🧪 RAG evaluation
- 📋 Automated 20-question evaluation suite
- 🔗 GOV.UK source attribution
- 🧠 Simple conversation memory
- 📱 Responsive React interface
- ⚡ FastAPI REST API
- 🔐 CORS-enabled frontend/backend integration
- 💰 No paid external AI API required for local development

---

# 🏗️ System Architecture

The current VisaPath architecture is:

```
                         VisaPath
                            │
             ┌──────────────┴──────────────┐
             │                             │
             ▼                             ▼
      React / Vite                    FastAPI
       Frontend                      Backend API
                                           │
                                           ▼
                                  Query Processing
                                           │
                                           ▼
                                  Chroma Vector DB
                                           │
                                           ▼
                                  GOV.UK Documents
                                           │
                                           ▼
                                  Retrieved Context
                                           │
                                           ▼
                                  Grounded Prompt
                                           │
                                           ▼
                                  LangChain
                                           │
                                           ▼
                                    ChatOllama
                                           │
                                           ▼
                                     Llama 3.2
                                           │
                                           ▼
                                  Generated Answer
                                           │
                            ┌──────────────┴──────────────┐
                            │                             │
                            ▼                             ▼
                       User Response              Evaluation Layer
                                                          │
                                            ┌─────────────┴─────────────┐
                                            ▼                           ▼
                                      Faithfulness                 RAG Score
                                            │                           │
                                            └─────────────┬─────────────┘
                                                          ▼
                                                       Langfuse
```

---

# 🔄 Request Flow

A typical user request follows this process:

1. The user enters a question in the React frontend.
2. React sends the question to the FastAPI `/chat` endpoint.
3. FastAPI receives the question.
4. The question is sent to the RAG retrieval layer.
5. Chroma performs semantic similarity search against the GOV.UK document collection.
6. The most relevant documents are retrieved.
7. The retrieved content and source URLs are added to the generation prompt.
8. LangChain sends the grounded prompt to Ollama.
9. Ollama runs the Llama 3.2 model locally.
10. The model generates an answer using the retrieved context.
11. A faithfulness evaluator checks whether the answer is supported by the retrieved context.
12. A separate RAG evaluator assesses the overall quality of the answer.
13. Scores are sent to Langfuse.
14. The API returns the answer, sources, and faithfulness score.
15. React displays the response to the user.

---

# 🛠️ Technology Stack

## Frontend

- React
- Vite
- JavaScript
- CSS
- HTML

## Backend

- Python
- FastAPI
- Uvicorn
- Pydantic

## AI / LLM

- Ollama
- Llama 3.2
- LangChain
- `ChatOllama`

## RAG

- Chroma
- LangChain Chroma integration
- `OllamaEmbeddings`
- `nomic-embed-text`
- Semantic similarity search
- GOV.UK reference documents

## Observability

- Langfuse
- OpenTelemetry-based tracing through the Langfuse SDK
- Retrieval tracing
- LLM generation tracing
- Evaluation scores

## Evaluation

- Faithfulness evaluation
- RAG evaluation
- 20-question evaluation dataset
- Automated evaluation script

## Development Environment

- Windows
- Python virtual environment
- Node.js
- npm
- Git
- GitHub

---

# 📋 Requirements

Before running VisaPath locally, install the following.

## Python

Python 3.10+ is recommended.

Check your installation:

```
python --version
```

Example:

```
Python 3.11.x
```

---

## Node.js

Node.js 18+ is recommended.

Check:

```
node --version
npm --version
```

---

## Ollama

Install Ollama from:

https://ollama.com/

Check the installation:

```
ollama --version
```

Example:

```
ollama version is 0.34.3
```

---

# 🤖 AI Model Setup

VisaPath currently uses:

```
llama3.2:latest
```

Download the model:

```
ollama pull llama3.2
```

Check installed models:

```
ollama list
```

You should see something similar to:

```
NAME              SIZE
llama3.2:latest   2.0 GB
```

Ollama must be running while using the chatbot.

---

# 🧠 Embedding Model

The RAG pipeline uses:

```
nomic-embed-text
```

The embedding model converts user questions and reference documents into vectors so that semantically relevant information can be retrieved.

Pull the embedding model:

```
ollama pull nomic-embed-text
```

Check:

```
ollama list
```

You should see both:

```
llama3.2
nomic-embed-text
```

---

# 📁 Project Structure

The project is organized into separate frontend and backend applications.

```
ai-visa-assistant/
│
├── backend/
│   ├── main.py
│   ├── evaluate.py
│   ├── requirements.txt
│   ├── chroma_db/
│   │
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
│   │
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── index.html
│
└── README.md
```

---

# 🚀 Backend Setup

Open a terminal and navigate to the backend:

```
cd backend
```

---

## Create a Virtual Environment

Windows:

```
python -m venv .venv
```

Activate it:

```
.venv\Scripts\activate
```

After activation you should see:

```
(.venv)
```

---

# 📦 Install Backend Dependencies

The backend uses:

- FastAPI
- Uvicorn
- LangChain
- Ollama integration
- Chroma
- Langfuse

Install the dependencies:

```
pip install -r requirements.txt
```

If installing manually:

```
pip install fastapi uvicorn langchain langchain-ollama langchain-chroma chromadb langfuse
```

---

# 🔐 Langfuse Configuration

Langfuse is used to monitor and evaluate the RAG pipeline.

The application expects Langfuse credentials to be configured as environment variables.

Typical configuration:

```
LANGFUSE_PUBLIC_KEY
LANGFUSE_SECRET_KEY
LANGFUSE_HOST
```

For example:

```
LANGFUSE_HOST=https://cloud.langfuse.com
```

Do not commit Langfuse credentials to GitHub.

Use environment variables or a local `.env` file that is excluded from version control.

Example:

```
.env
```

should be included in `.gitignore`.

---

# ▶️ Run the Backend

From the backend directory:

```
uvicorn main:app --reload
```

The backend should start at:

```
http://127.0.0.1:8000
```

You should see:

```
Application startup complete.
```

---

# 🔌 Backend API

VisaPath exposes a FastAPI REST API.

## GET /

The root endpoint checks that the API is running.

Example:

```
GET http://127.0.0.1:8000/
```

---

## GET /health

Health check endpoint.

Example:

```
GET http://127.0.0.1:8000/health
```

Expected response:

```
{
  "status": "ok"
}
```

---

# 💬 POST /chat

The `/chat` endpoint accepts a user question and returns a grounded AI response.

## Request

```
{
  "message": "I want to work in the UK. What visa options might I have?"
}
```

## Example Response

```
{
  "response": "You may be eligible for a Skilled Worker visa or a Health and Care Worker visa, depending on your job and employer.",
  "sources": [
    "https://www.gov.uk/skilled-worker-visa",
    "https://www.gov.uk/health-care-worker-visa"
  ],
  "faithfulness_score": 1.0,
  "rag_score": 1.0
}
```

The exact answer and source list depend on the retrieved context.

---

# 📚 API Documentation

FastAPI automatically provides interactive API documentation.

After starting the backend, open:

```
http://127.0.0.1:8000/docs
```

This provides a Swagger interface where the `/chat` endpoint can be tested directly.

---

# 🧠 Retrieval-Augmented Generation

VisaPath uses RAG to reduce unsupported model responses.

Instead of asking the LLM to answer directly from its pretrained knowledge, the application first retrieves relevant GOV.UK information.

The process is:

```
Question
   ↓
Embedding
   ↓
Vector Search
   ↓
Relevant GOV.UK Documents
   ↓
Context
   ↓
Grounded Prompt
   ↓
Llama 3.2
   ↓
Answer
```

---

# 🗄️ Chroma Vector Database

Chroma stores the embedded GOV.UK reference documents.

The backend initializes the vector database using:

```
vectorstore = Chroma(
    persist_directory=CHROMA_DIR,
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings,
)
```

The current configuration uses:

```
CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "visapath"
```

---

# 🔎 Retrieval

The RAG system performs semantic similarity search.

Current configuration:

```
TOP_K = 6
```

The backend retrieves the six most relevant documents for a question.

Each retrieved document contains:

```
content
source
```

The source is the GOV.UK URL associated with the reference material.

---

# 🧩 Embeddings

VisaPath uses:

```
nomic-embed-text
```

through LangChain:

```
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)
```

The embedding model is used to represent both queries and documents as vectors.

This allows the application to retrieve semantically related content even when the wording of the question does not exactly match the wording in the source document.

---

# 🤖 LangChain + Ollama

The LLM is accessed through LangChain's Ollama integration.

Example:

```
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
)
```

The model receives the system instructions, retrieved GOV.UK context, and the user's question.

---

# 🛡️ Hallucination Control

VisaPath includes explicit grounding rules in the system prompt.

The assistant is instructed to:

- Use only retrieved GOV.UK information.
- Never use unsupported outside knowledge.
- Never invent visa requirements.
- Never invent fees.
- Never invent salary thresholds.
- Never invent processing times.
- Never invent eligibility requirements.
- Avoid combining unrelated visa requirements.
- Never claim that a user is personally eligible.
- Say when the available context is insufficient.
- Avoid presenting itself as a legal adviser.

The key principle is:

```
No evidence in retrieved context
            ↓
Do not make the claim
```

This provides a controlled boundary around the LLM's normal tendency to use its pretrained knowledge.

---

# 📖 Grounded Generation

The retrieved documents are inserted into the prompt together with their source URLs.

Conceptually:

```
SYSTEM INSTRUCTIONS

        +

GOV.UK REFERENCE CONTEXT

        +

USER QUESTION

        ↓

     Llama 3.2

        ↓

Grounded Answer
```

The model is explicitly told that factual claims must be supported by the supplied context.

---

# 🔗 Source Attribution

The backend returns the sources associated with retrieved documents.

Example:

```
{
  "sources": [
    "https://www.gov.uk/skilled-worker-visa",
    "https://www.gov.uk/health-care-worker-visa"
  ]
}
```

This provides traceability between the generated response and the reference material.

The source URLs are official GOV.UK pages.

---

# 📊 Langfuse Observability

VisaPath integrates Langfuse to provide observability across the RAG pipeline.

The system records operations including:

```
chat
 ├── rag-retrieval
 ├── ollama-generation
 ├── faithfulness-evaluation
 └── rag-evaluation
```

This makes it possible to inspect:

- User questions
- Retrieved documents
- Retrieval latency
- Generated answers
- LLM generation latency
- Evaluation scores
- Source information
- Individual traces

This is useful when debugging both retrieval and generation quality.

---

# 🔬 Faithfulness Evaluation

After generating an answer, VisaPath evaluates whether the answer is actually supported by the retrieved context.

The evaluator receives:

```
GOV.UK Context
       +
Generated Answer
```

It then assigns a score.

Possible scores:

```
1.0
0.75
0.50
0.25
0.0
```

Meaning:

```
1.0
All important factual claims are supported.

0.75
Almost all important claims are supported,
with minor unsupported details.

0.50
Some important claims are supported,
but meaningful unsupported claims exist.

0.25
Most important claims are unsupported.

0.0
The answer is substantially unsupported.
```

The faithfulness score is also recorded in Langfuse.

---

# 🎯 RAG Evaluation

VisaPath also evaluates the overall RAG answer separately from the faithfulness check.

The RAG evaluator considers:

1. Whether the answer addresses the question.
2. Whether it uses retrieved information.
3. Whether unsupported claims are avoided.
4. Whether information has been invented.
5. Whether visa requirements have been incorrectly combined.
6. Whether the assistant acknowledges missing information.

The evaluator returns:

```
1.0
0.75
0.50
0.25
0.0
```

---

# 🧪 Automated 20-Question Evaluation

VisaPath includes a 20-question evaluation suite.

The questions cover:

- Skilled Worker visa
- Skilled Worker requirements
- Certificate of Sponsorship
- Visa duration
- Visa extension
- English requirements
- Health and Care Worker visa
- Health and Care Worker requirements
- Settlement
- Youth Mobility Scheme
- Youth Mobility work permissions
- Global Talent
- Skilled Worker costs
- Changing employers
- General work visa questions

The evaluation can be run with:

```
python evaluate.py
```

---

# 📈 Evaluation Results

The current evaluation contains:

```
20 questions
```

The latest evaluation produced:

```
======================================================================
FINAL RESULTS
======================================================================

Questions evaluated:     20
Average faithfulness:     1.00
Average RAG score:        0.94

Faithfulness 1.0:         20/20
RAG score 1.0:            18/20

======================================================================
Evaluation complete.
======================================================================
```

### Interpretation

**Faithfulness: 1.00**

All 20 evaluated responses were judged fully supported by the supplied context.

**RAG score: 0.94**

The overall RAG evaluation was strong, with 18 out of 20 questions receiving a perfect score.

Two questions received lower RAG scores:

```
Question 16:
Can you work while on the Youth Mobility Scheme visa?

RAG: 0.00

Question 18:
How much does a Skilled Worker visa cost?

RAG: 0.75
```

These are useful regression-test cases because they identify areas where retrieval or answer completeness could be improved.

---

# 🧪 Running the Evaluation

Start the backend first.

Then from the backend directory:

```
python evaluate.py
```

The script sends the evaluation questions through the RAG pipeline and reports:

- Individual faithfulness scores
- Individual RAG scores
- Retrieved source count
- Average faithfulness
- Average RAG score
- Number of perfect evaluations

---

# 📋 Example Evaluation Output

```
======================================================================
VisaPath - RAG Evaluation
======================================================================

[1/20] What is a Skilled Worker visa?

...

======================================================================
FINAL RESULTS
======================================================================

Questions evaluated:     20
Average faithfulness:     1.00
Average RAG score:        0.94
Faithfulness 1.0:         20/20
RAG score 1.0:             18/20

======================================================================
QUESTION RESULTS
======================================================================

01. What is a Skilled Worker visa?
    Faithfulness: 1.00
    RAG:          1.00

02. What are the main requirements for a Skilled Worker visa?
    Faithfulness: 1.00
    RAG:          1.00

...

20. What UK visa should I get if I have a job offer?
    Faithfulness: 1.00
    RAG:          1.00

======================================================================
Evaluation complete.
======================================================================
```

---

# 🧠 Conversation Memory

VisaPath also supports simple conversation memory.

Recent messages can be supplied to the model so that follow-up questions have conversational context.

For example:

```
User:
What is a Skilled Worker visa?

Assistant:
...

User:
How long can it last?

Assistant:
...
```

The application can retain recent conversation context rather than sending the entire conversation history.

Conversation state is currently stored in application memory.

Therefore:

- It is not persistent.
- It can be lost when the backend restarts.
- It is not suitable for multi-user production deployments.

---

# 💻 Frontend Setup

Open another terminal:

```
cd frontend
```

Install dependencies:

```
npm install
```

---

# ▶️ Run the Frontend

Start Vite:

```
npm run dev
```

Vite will normally provide:

```
http://localhost:5173
```

Open the address in your browser.

---

# 🔌 Frontend → Backend Integration

The React frontend communicates with FastAPI through the `/chat` endpoint.

Example:

```
fetch("http://127.0.0.1:8000/chat", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    message: question
  })
});
```

The backend returns:

```
{
  "response": "...",
  "sources": [],
  "faithfulness_score": 1.0,
  "rag_score": 1.0
}
```

The frontend displays the generated response.

---

# 🎨 UI Design

VisaPath uses a simple conversational interface designed around:

- Neutral earthy colours
- Warm ivory backgrounds
- Beige message areas
- Charcoal text
- Muted brown primary controls
- Rounded chat cards
- Clear spacing
- Responsive layout
- Simple navigation

The interface is intentionally lightweight so the conversation remains the main focus.

---

# 🧪 Manual API Testing

The backend can be tested directly from Windows Command Prompt.

Start the backend:

```
uvicorn main:app --reload
```

Then run:

```
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d "{\"message\":\"I want to work in the UK. What visa options might I have?\"}"
```

Example response:

```
{
  "response": "You may be eligible for a Skilled Worker visa or a Health and Care Worker visa, depending on your job and employer.",
  "sources": [
    "https://www.gov.uk/skilled-worker-visa",
    "https://www.gov.uk/health-care-worker-visa"
  ],
  "faithfulness_score": 1.0,
  "rag_score": 1.0
}
```

---

# 🧪 Testing Through Swagger

Alternatively, open:

```
http://127.0.0.1:8000/docs
```

Find:

```
POST /chat
```

Select:

```
Try it out
```

Enter:

```
{
  "message": "I want to work in the UK. What visa options might I have?"
}
```

Then select:

```
Execute
```

The response will include the generated answer, sources, and evaluation scores.

---

# 🔍 Testing the RAG Pipeline

A useful development question is:

```
I want to work in the UK. What visa options might I have?
```

The retrieval system should identify relevant GOV.UK material such as:

```
Skilled Worker visa
Health and Care Worker visa
Youth Mobility Scheme
```

The final answer should only make claims supported by the retrieved material.

---

# ⚖️ Official GOV.UK Sources

VisaPath is designed around official UK Government reference material.

Useful official sources include:

## UK Visas and Immigration

https://www.gov.uk/browse/visas-immigration

## Skilled Worker visa

https://www.gov.uk/skilled-worker-visa

## Health and Care Worker visa

https://www.gov.uk/health-care-worker-visa

## Youth Mobility Scheme

https://www.gov.uk/youth-mobility

Users should always verify current requirements against GOV.UK because immigration rules can change.

---

# 🔐 Security Considerations

The project is intended for local development and demonstration.

Do not commit:

```
.env
API keys
Langfuse secret keys
private credentials
production configuration
private datasets
```

Use environment variables for secrets.

For example:

```
LANGFUSE_PUBLIC_KEY=...
LANGFUSE_SECRET_KEY=...
LANGFUSE_HOST=...
```

Add sensitive files to `.gitignore`.

---

# ⚠️ Known Limitations

VisaPath is currently a development/portfolio application.

It does not currently provide:

- User authentication
- Persistent user accounts
- Production database storage
- Production deployment
- Automated GOV.UK rule updates
- Professional immigration advice
- Guaranteed legal accuracy
- Automated source freshness checking
- Streaming AI responses
- Request cancellation/stop button
- Production-grade multi-user conversation storage

The RAG system also depends on the quality and freshness of the documents stored in the Chroma database.

The evaluation system provides useful development metrics but should not be interpreted as proof of legal or factual correctness in every real-world scenario.

---

# 🔮 Future Improvements

Potential future improvements include:

## Retrieval

- Hybrid keyword + vector search
- Document reranking
- Improved chunking
- Metadata filtering
- Better query expansion
- Retrieval hit-rate evaluation
- Larger evaluation datasets

## Data

- Automated GOV.UK document updates
- Document version tracking
- Source freshness monitoring
- Automatic re-indexing

## AI

- Improved answer citation
- Structured visa-route classification
- Better uncertainty handling
- More robust claim-level verification

## UX

- Streaming responses
- Stop/cancel generation
- Better loading states
- Conversation history
- User accounts

## Infrastructure

- Persistent database
- Authentication
- Production deployment
- Monitoring and alerting
- Automated CI/CD

---

# 📊 Development Metrics

Current development baseline:

| Metric | Result |
| --- | --- |
| Evaluation questions | 20 |
| Average faithfulness | **1.00** |
| Average RAG score | **0.94** |
| Faithfulness 1.0 | **20/20** |
| RAG score 1.0 | **18/20** |

These metrics provide a baseline for future improvements.

---

# 🧑‍💻 Development Philosophy

VisaPath was developed incrementally.

The original application started as a straightforward local LLM application:

```
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
```

The application was then extended with retrieval:

```
React
  ↓
FastAPI
  ↓
Chroma
  ↓
GOV.UK Context
  ↓
Ollama / Llama 3.2
  ↓
Response
```

The current system adds evaluation and observability:

```
                         ┌───────────────┐
                         │    React      │
                         │    Frontend   │
                         └───────┬───────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │    FastAPI    │
                         └───────┬───────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
                    ▼                         ▼
             ┌───────────────┐       ┌───────────────┐
             │    Chroma     │       │   Langfuse    │
             │  Vector DB    │       │  Observability│
             └───────┬───────┘       └───────────────┘
                     │
                     ▼
             ┌───────────────┐
             │ GOV.UK Context│
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │   LangChain   │
             │   ChatOllama  │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │   Llama 3.2   │
             └───────┬───────┘
                     │
                     ▼
             ┌─────────────────────┐
             │ Generated Response  │
             └──────────┬──────────┘
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
      ┌──────────────┐      ┌──────────────┐
      │ Faithfulness │      │ RAG Evaluation│
      │ Evaluation   │      │              │
      └──────┬───────┘      └──────┬───────┘
             │                     │
             └──────────┬──────────┘
                        ▼
                    Langfuse
```

The goal is to demonstrate that an LLM application is not just about generating text. A useful production-oriented AI system also needs:

- Relevant retrieval
- Grounding
- Source attribution
- Evaluation
- Observability
- Error analysis
- Iterative improvement

---

# 📊 Project Status

## Current Status: Working RAG-Based AI Application

VisaPath currently demonstrates:

- Full-stack React/FastAPI development
- Local LLM inference
- Ollama integration
- Llama 3.2
- LangChain
- Chroma vector search
- RAG
- GOV.UK reference retrieval
- Grounded generation
- Hallucination controls
- Source attribution
- Langfuse tracing
- Faithfulness evaluation
- RAG evaluation
- Automated 20-question evaluation
- Frontend/backend integration
- Responsive UI
- Local development workflow

Current evaluation baseline:

```
Faithfulness: 1.00
RAG score:    0.94
```

---

# 🧑‍💻 Project Scope

VisaPath demonstrates practical experience with:

- Full-stack application development
- React
- Vite
- FastAPI
- REST APIs
- Python
- LangChain
- Ollama
- Llama 3.2
- Embeddings
- Vector databases
- Chroma
- Retrieval-Augmented Generation
- Prompt engineering
- Grounded generation
- Hallucination control
- LLM evaluation
- Faithfulness evaluation
- RAG evaluation
- Langfuse observability
- Source attribution
- Conversational AI
- Responsive UI development
- API design
- Git/GitHub workflows
- Local AI development

---

# 🎯 What This Project Demonstrates

The project demonstrates an end-to-end AI engineering workflow:

```
Build
  ↓
Retrieve
  ↓
Generate
  ↓
Observe
  ↓
Evaluate
  ↓
Identify Weaknesses
  ↓
Improve
```

Rather than relying only on an LLM's pretrained knowledge, VisaPath uses a retrieval layer and evaluation pipeline to make the system more grounded and measurable.

The current 20-question evaluation provides a reproducible baseline for future changes.

---

# 🚀 Running the Complete Application

VisaPath requires three main components during local development.

## Terminal 1 — Ollama

Make sure Ollama is installed and the models are available:

```
ollama list
```

Confirm:

```
llama3.2
nomic-embed-text
```

Ollama should remain running.

---

## Terminal 2 — Backend

```
cd backend
```

Activate the virtual environment:

```
.venv\Scripts\activate
```

Start FastAPI:

```
uvicorn main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

## Terminal 3 — Frontend

```
cd frontend
```

Install dependencies if necessary:

```
npm install
```

Start Vite:

```
npm run dev
```

Frontend:

```
http://localhost:5173
```

---

# 🧪 Run the Evaluation

With the backend and Ollama available:

```
cd backend
.venv\Scripts\activate
python evaluate.py
```

Expected evaluation structure:

```
Questions evaluated: 20

Average faithfulness: 1.00
Average RAG score:    0.94
```

---

# 📝 Example User Questions

The following questions can be used to test VisaPath:

```
What is a Skilled Worker visa?

What are the main requirements for a Skilled Worker visa?

Do I need a confirmed job offer for a Skilled Worker visa?

What is a Certificate of Sponsorship?

How long can a Skilled Worker visa last?

Can I extend a Skilled Worker visa?

What English language requirement applies to a Skilled Worker visa?

What is a Health and Care Worker visa?

Do I need a confirmed job offer for a Health and Care Worker visa?

How long can a Health and Care Worker visa last?

Can a Health and Care Worker visa be extended?

Can someone on a Health and Care Worker visa eventually apply to settle?

What is the Youth Mobility Scheme visa?

How long can you stay under the Youth Mobility Scheme?

What can you do while on the Youth Mobility Scheme visa?

Can you work while on the Youth Mobility Scheme visa?

What is the Global Talent visa?

How much does a Skilled Worker visa cost?

Can I change my employer while on a Skilled Worker visa?

What UK visa should I get if I have a job offer?
```

---

# 📌 Important Design Principle

VisaPath does not attempt to make the LLM the final authority.

The intended architecture is:

```
Official Reference Material
          ↓
       Retrieval
          ↓
   Grounded Generation
          ↓
      Evaluation
          ↓
       Response
```

This makes the system more transparent and measurable than a standalone LLM chatbot.

---

# ⚖️ Final Disclaimer

VisaPath is an AI-powered informational tool for educational and demonstration purposes.

It does not provide legal advice.

It does not determine whether an individual qualifies for a UK visa.

Immigration requirements can change over time.

Users should verify important information using current official GOV.UK guidance and seek professional immigration advice where appropriate.

---

# 👨‍💻 Project Status

**VisaPath — Working RAG-Based AI Application**

Current baseline:

```
RAG                         ✅
Chroma                      ✅
LangChain                   ✅
Ollama                      ✅
Llama 3.2                   ✅
GOV.UK retrieval            ✅
Grounding controls          ✅
Source attribution          ✅
Langfuse tracing            ✅
Faithfulness evaluation     ✅
RAG evaluation              ✅
20-question evaluation      ✅
React frontend              ✅
FastAPI backend              ✅

Streaming                   🔮 Future
Request cancellation       🔮 Future
Production deployment      🔮 Future
Automated GOV.UK updates   🔮 Future
```

---

## 📈 Evaluation Baseline

```
20 evaluation questions

Average Faithfulness: 1.00
Average RAG Score:    0.94

20/20 Faithfulness = 1.00
18/20 RAG Score     = 1.00
```

This baseline can be used to measure the impact of future retrieval, prompt, embedding, model, and evaluation improvements.

