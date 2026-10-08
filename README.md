# VisaPath

### AI-Powered UK Immigration Information Assistant

VisaPath is a full-stack conversational AI application designed to help users explore **UK visa and immigration information** through a simple chat interface.

The application combines a **React/Vite frontend**, **FastAPI backend**, **Ollama-powered local LLM inference**, and a **Retrieval-Augmented Generation (RAG) pipeline using Chroma and LangChain**.

The project also includes **Langfuse observability and evaluation**, allowing AI responses, retrieval, faithfulness, and RAG quality to be monitored and evaluated.

> **Project Notice** This repository is a sanitised version of a project originally developed as part of my work at a previous company. Company-specific information, proprietary implementation details, credentials, production configuration, confidential data, and other sensitive information have been removed or modified.

---

# 📌 Overview

VisaPath allows users to ask questions about UK immigration and receive conversational, grounded AI guidance based on retrieved **GOV.UK reference information**.

The application has evolved from a simple local LLM chatbot into a small **RAG-based AI application with observability and evaluation**.

The current architecture is:

```
User
  ↓
React / Vite Frontend
  ↓
FastAPI Backend
  ↓
RAG Retrieval
  ↓
Chroma Vector Database
  ↓
GOV.UK Reference Content
  ↓
Relevant Context
  ↓
LangChain / Ollama
  ↓
Llama 3.2
  ↓
Grounded AI Response
  ↓
Faithfulness Evaluation
  ↓
RAG Evaluation
  ↓
Langfuse Observability
  ↓
React Chat Interface
```

The system is designed to reduce hallucinations by instructing the model to answer using **only the retrieved GOV.UK reference context**.

---

# ✨ Features

## AI & RAG

- 💬 Conversational UK immigration assistant
- 🤖 Local AI inference using Ollama
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 GOV.UK reference knowledge base
- 🔎 Semantic document retrieval using embeddings
- 🗄️ Chroma vector database
- 🔗 LangChain integration
- 🎯 Top-K context retrieval
- 🛡️ Hallucination-control prompt
- 📖 Source-aware responses

## Evaluation & Observability

- 📊 Langfuse tracing
- 🔍 RAG retrieval tracing
- 🤖 LLM generation tracing
- 🧪 Faithfulness evaluation
- 📈 RAG answer evaluation
- 📝 20-question evaluation dataset
- 📊 Automated evaluation script
- 📉 Retrieval/evaluation metrics
- 🔗 Source tracking for generated answers

## Application

- ⚛️ React/Vite frontend
- ⚡ FastAPI REST API
- 🔄 Follow-up questions
- 🧠 Lightweight conversation context
- 📱 Responsive chat interface
- 🔗 Official GOV.UK sources
- 🔐 CORS-enabled frontend/backend communication
- 💰 Local AI inference without external AI API costs during development

---

# 🏗️ System Architecture

```
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
                                          ▼
                                  Query Processing
                                          │
                                          ▼
                                Chroma Vector Store
                                          │
                                          ▼
                                Semantic Retrieval
                                          │
                                          ▼
                              GOV.UK Reference Context
                                          │
                                          ▼
                                LangChain / Ollama
                                          │
                                          ▼
                                  llama3.2:latest
                                          │
                                          ▼
                                  Generated Answer
                                          │
                              ┌───────────┴───────────┐
                              │                       │
                              ▼                       ▼
                       Faithfulness              RAG Evaluation
                       Evaluation                 Evaluation
                              │                       │
                              └───────────┬───────────┘
                                          ▼
                                       Langfuse
                                          │
                                          ▼
                                   React Chat UI
```

---

# 🔄 Request Flow

When a user asks a question:

```
1. User enters a question
        ↓
2. React sends POST /chat
        ↓
3. FastAPI receives the question
        ↓
4. Query is embedded
        ↓
5. Chroma performs semantic retrieval
        ↓
6. Relevant GOV.UK documents are selected
        ↓
7. Retrieved context is added to the LLM prompt
        ↓
8. Ollama / Llama 3.2 generates the answer
        ↓
9. Faithfulness evaluator checks grounding
        ↓
10. RAG evaluator checks answer quality
        ↓
11. Scores are recorded in Langfuse
        ↓
12. Response and source URLs are returned
        ↓
13. React displays the answer
```

---

# 🤖 AI Model

VisaPath currently uses:

```
llama3.2:latest
```

The model runs locally through **Ollama**.

The backend uses the LangChain Ollama integration:

```
from langchain_ollama import ChatOllama
```

The LLM is configured with deterministic generation:

```
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
)
```

A low/zero temperature is used to make responses more consistent and reduce unnecessary variation.

---

# 🧠 Retrieval-Augmented Generation

VisaPath now uses **Retrieval-Augmented Generation (RAG)** rather than relying solely on the LLM's internal knowledge.

The purpose of the RAG layer is to provide the model with relevant GOV.UK reference information before generating an answer.

## RAG Pipeline

```
User Question
      ↓
Embedding
      ↓
Vector Search
      ↓
Chroma
      ↓
Top-K GOV.UK Documents
      ↓
Context Construction
      ↓
Grounded LLM Prompt
      ↓
Answer
```

The current retrieval configuration uses:

```
TOP_K = 6
```

The backend retrieves the most relevant documents using semantic similarity.

---

# 📚 Knowledge Base

The RAG system uses GOV.UK immigration information as its reference material.

Example sources include:

```
https://www.gov.uk/skilled-worker-visa
https://www.gov.uk/health-care-worker-visa
https://www.gov.uk/youth-mobility
```

Retrieved documents contain both:

```
content
source
```

This allows the application to return the source URLs associated with the retrieved context.

---

# 🗄️ Vector Database

VisaPath uses **Chroma** for vector storage and semantic retrieval.

Configuration:

```
CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "visapath"
```

Embeddings are generated using:

```
nomic-embed-text
```

through Ollama.

The backend initializes the vector store using:

```
from langchain_chroma import Chroma
```

and:

```
vectorstore = Chroma(
    persist_directory=CHROMA_DIR,
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings,
)
```

---

# 🔎 Retrieval

The retrieval layer is implemented as a dedicated function:

```
@observe(name="rag-retrieval")
def retrieve_context(query: str, top_k: int = TOP_K):
```

This function:

1. Accepts the user question
2. Performs semantic similarity search
3. Retrieves the most relevant documents
4. Extracts document content
5. Preserves source URLs
6. Returns structured context to the generation layer

Example:

```
Question:
"I want to work in the UK. What visa options might I have?"

Retrieved sources:

1. GOV.UK Skilled Worker visa
2. GOV.UK Health and Care Worker visa
3. GOV.UK Youth Mobility Scheme
```

---

# 🛡️ Hallucination Control

The LLM is given a strict grounding prompt.

The system instructs the model to:

- Use only retrieved GOV.UK context
- Never rely on outside knowledge
- Never invent visa requirements
- Never invent fees
- Never invent salary thresholds
- Never invent processing times
- Never assume eligibility
- Avoid combining requirements from unrelated visa routes
- State when the retrieved information is insufficient
- Avoid presenting itself as a solicitor
- Keep factual claims grounded in the supplied context

The central principle is:

```
Retrieved Context
       ↓
      LLM
       ↓
Only supported claims
```

If the retrieved material does not contain enough information, the assistant is instructed to say:

```
I don't have enough information in the GOV.UK reference
material to answer that accurately.
```

This provides an additional layer of protection against unsupported model-generated information.

---

# 📊 Langfuse Observability

VisaPath now includes **Langfuse** for AI observability.

Langfuse provides visibility into the RAG pipeline and LLM execution.

The application traces:

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
- Source URLs
- LLM prompts
- Generated responses
- Retrieval latency
- Generation latency
- Evaluation scores
- Overall traces

---

# 🔍 Faithfulness Evaluation

VisaPath includes a dedicated faithfulness evaluator.

The evaluator checks whether the generated response is supported by the retrieved GOV.UK context.

The evaluator does **not** use outside knowledge.

It evaluates whether claims in the answer are supported by the supplied context.

The scoring scale is:

```
1.00  = All important factual claims are supported
0.75  = Almost all claims are supported
0.50  = Some important claims are supported
0.25  = Most important claims are unsupported
0.00  = Answer is substantially unsupported
```

The score is recorded in Langfuse using:

```
faithfulness
```

---

# 📈 RAG Evaluation

A second evaluator measures overall RAG answer quality.

It evaluates whether the answer:

1. Answers the user's question
2. Uses the retrieved context
3. Avoids unsupported claims
4. Avoids invented information
5. Avoids incorrectly combining visa requirements
6. Clearly handles missing information

The scoring scale is:

```
1.00  = Excellent grounded answer
0.75  = Good answer with minor issues
0.50  = Partially correct or grounded
0.25  = Major problems
0.00  = Incorrect or unsupported
```

The score is recorded in Langfuse using:

```
rag_evaluation
```

---

# 🧪 RAG Evaluation Dataset

VisaPath includes a small automated evaluation suite containing **20 representative immigration questions**.

The questions cover areas such as:

- Skilled Worker visa
- Certificate of Sponsorship
- English requirements
- Visa duration
- Visa extensions
- Health and Care Worker visa
- Settlement
- Youth Mobility Scheme
- Global Talent
- Visa costs
- Changing employers
- General work visa questions

The evaluation can be run using:

```
python evaluate.py
```

---

# 📊 Evaluation Results

The current 20-question evaluation produced:

```
Questions evaluated:     20

Average faithfulness:    1.00
Average RAG score:       0.94

Faithfulness 1.0:        20/20
RAG score 1.0:           18/20
```

This means the current evaluation run achieved:

### Faithfulness

```
100% of evaluated responses received
a faithfulness score of 1.00
```

### RAG Evaluation

```
18/20 responses received a perfect RAG score.

Average RAG score:
0.94
```

Two questions produced lower RAG scores:

```
Youth Mobility Scheme work question → 0.00
Skilled Worker visa cost question  → 0.75
```

These results are useful because they identify areas where the retrieval dataset or evaluation criteria can be improved rather than simply assuming that every answer is correct.

> Evaluation scores are based on the current local evaluation dataset and should not be interpreted as a guarantee of real-world immigration accuracy.

---

# 🧪 Example Evaluation Output

```
======================================================================
VisaPath - RAG Evaluation
======================================================================

Questions evaluated:     20
Average faithfulness:    1.00
Average RAG score:       0.94
Faithfulness 1.0:        20/20
RAG score 1.0:           18/20
```

This evaluation provides a repeatable baseline for future RAG improvements.

---

# 🧠 Conversation Memory

VisaPath also maintains lightweight conversation context.

Recent messages can be passed to the model to support follow-up questions.

Example:

```
User:
I want to work in the UK.

Assistant:
A Skilled Worker visa may be relevant if...

User:
What about the English requirement?

Assistant:
The retrieved GOV.UK information states that...
```

Conversation memory remains lightweight and is currently held in application memory.

It is not yet persisted in a database.

---

# 🔗 Source Tracking

Each retrieved document includes its source URL.

The API response therefore includes the unique GOV.UK sources used during retrieval.

Example:

```
{
  "response": "You may be eligible for a Skilled Worker visa or a Health and Care Worker visa, depending on your circumstances.",
  "sources": [
    "https://www.gov.uk/skilled-worker-visa",
    "https://www.gov.uk/health-care-worker-visa",
    "https://www.gov.uk/youth-mobility"
  ],
  "faithfulness_score": 1.0,
  "rag_score": 1.0
}
```

This improves transparency by allowing users or developers to inspect the underlying official references.

---

# 📁 Project Structure

```
visapath-ai-chatbot/
│
├── backend/
│   ├── main.py
│   ├── evaluate.py
│   ├── requirements.txt
│   ├── chroma_db/
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
├── PROJECT_DOCUMENTATION.md
├── README.md
└── .gitignore
```

---

# 📋 Requirements

Before running VisaPath locally, install:

- Python 3.10+
- Node.js 18+
- Ollama
- Git

The backend additionally requires:

- FastAPI
- Uvicorn
- LangChain
- LangChain Ollama
- LangChain Chroma
- ChromaDB
- Langfuse

---

# 🚀 Getting Started

## 1\. Install Ollama

Install Ollama and ensure it is running.

Pull the required models:

```
ollama pull llama3.2
ollama pull nomic-embed-text
```

Verify:

```
ollama list
```

You should see models similar to:

```
llama3.2:latest
nomic-embed-text
```

---

# 2\. Backend Setup

Navigate to the backend:

```
cd backend
```

Create a virtual environment:

```
python -m venv .venv
```

Activate it on Windows:

```
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# 3\. Langfuse Configuration

If Langfuse observability is enabled, configure the required environment variables.

Example:

```
LANGFUSE_PUBLIC_KEY=your-public-key
LANGFUSE_SECRET_KEY=your-secret-key
LANGFUSE_HOST=your-langfuse-host
```

Do not commit credentials to Git.

Use environment variables or a local `.env` file that is excluded from version control.

---

# 4\. Run the Backend

From the backend directory:

```
uvicorn main:app --reload
```

The backend should start at:

```
http://127.0.0.1:8000
```

---

# 5\. Run the Frontend

Open another terminal:

```
cd frontend
```

Install dependencies:

```
npm install
```

Run Vite:

```
npm run dev
```

The frontend will usually be available at:

```
http://localhost:5173
```

---

# 🔌 API

## `GET /`

Returns backend information.

Example:

```
{
  "status": "ok",
  "service": "VisaPath",
  "rag": "enabled",
  "hallucination_control": "enabled",
  "faithfulness_evaluation": "enabled",
  "rag_evaluation": "enabled"
}
```

---

# `GET /health`

Returns the health status of the service.

Example:

```
{
  "status": "ok"
}
```

---

# `POST /chat`

Sends a question to VisaPath.

### Request

```
{
  "message": "I want to work in the UK. What visa options might I have?"
}
```

### Response

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

The exact response and source list can vary depending on retrieval results.

---

# 📖 API Documentation

FastAPI automatically provides interactive Swagger documentation.

After starting the backend, open:

```
http://127.0.0.1:8000/docs
```

This can be used to:

- Inspect API endpoints
- Submit chat requests
- Inspect JSON responses
- Test the backend independently of the frontend

---

# 🧪 Testing the Chat API

On Windows, the backend can be tested using:

```
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d "{\"message\":\"I want to work in the UK. What visa options might I have?\"}"
```

Example:

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

# 🧪 Running the Evaluation

From the backend directory:

```
python evaluate.py
```

The evaluation runs the 20-question test suite and reports:

```
Average faithfulness
Average RAG score
Perfect faithfulness count
Perfect RAG score count
Per-question results
Retrieved source count
```

This provides a repeatable way to monitor changes to the RAG system.

---

# 🎨 User Interface

The frontend is designed around a simple conversational experience.

### Design characteristics

- Warm ivory background
- Neutral earthy colour palette
- Beige message areas
- Charcoal text
- Muted brown buttons
- Rounded chat cards
- Responsive layout
- Clear spacing and typography

The interface keeps the conversation as the primary interaction while allowing the backend to provide grounded responses.

---

# ⚠️ Current Limitations

VisaPath is currently a **working portfolio/MVP implementation**.

The application still does not include:

- Persistent user accounts
- Authentication
- Production deployment
- Persistent conversation database
- Automated GOV.UK data updates
- Production-grade source versioning
- Advanced retrieval reranking
- Hybrid keyword/vector retrieval
- Streaming AI responses
- Request cancellation/stop controls
- Large-scale evaluation datasets
- Human-reviewed immigration answer labels

The current evaluation suite contains 20 questions and is intended as an initial quality baseline rather than comprehensive immigration coverage.

---

# 🔮 Future Improvements

Potential future development includes:

## RAG

- Hybrid search
- Retrieval reranking
- Better document chunking
- Metadata filtering
- Query rewriting
- Improved retrieval hit-rate evaluation
- Larger evaluation datasets
- Human-labelled evaluation data
- Automated GOV.UK content updates

## AI

- Streaming responses
- Request cancellation
- Better conversational memory
- Structured eligibility flows
- Improved refusal/insufficient-context handling
- More granular claim-level faithfulness evaluation

## Infrastructure

- Persistent database
- User authentication
- Production deployment
- Background ingestion jobs
- Automated evaluation in CI/CD
- Monitoring and alerting
- Model/version tracking

## UX

- Clickable source citations
- Source previews
- Conversation history
- Structured visa comparison
- Eligibility questionnaires
- Improved mobile experience

---

# 📊 Project Status

**Status: Working RAG-enabled MVP**

VisaPath currently demonstrates:

```
React/Vite
     +
FastAPI
     +
LangChain
     +
Chroma
     +
Ollama
     +
Llama 3.2
     +
GOV.UK Reference Data
     +
Langfuse
     +
Faithfulness Evaluation
     +
RAG Evaluation
```

The project has progressed beyond a basic chatbot into an observable and evaluated RAG-based AI application.

---

# 🧑‍💻 Skills Demonstrated

This project demonstrates practical experience with:

### Full Stack

- React
- Vite
- JavaScript
- CSS
- Python
- FastAPI
- REST APIs
- CORS
- Frontend/backend integration

### AI Engineering

- Local LLM deployment
- Ollama
- Llama 3.2
- LangChain
- Prompt engineering
- Conversational AI
- Retrieval-Augmented Generation
- Embeddings
- Vector databases
- Semantic search
- Grounded generation
- Hallucination control

### AI Evaluation

- Langfuse
- LLM tracing
- RAG tracing
- Faithfulness evaluation
- RAG evaluation
- Evaluation datasets
- Automated evaluation scripts
- Retrieval/source tracking
- AI quality monitoring

### Development

- Python virtual environments
- Git/GitHub workflows
- Local development
- API testing
- Debugging
- Iterative AI system development

---

# 🔐 Security & Configuration

API credentials and secrets must not be committed to the repository.

Sensitive configuration should be stored using environment variables.

For example:

```
LANGFUSE_PUBLIC_KEY
LANGFUSE_SECRET_KEY
LANGFUSE_HOST
```

A `.gitignore` file should exclude:

```
.env
.venv/
__pycache__/
chroma_db/
```

depending on the intended repository setup.

---

# 🇬🇧 Official UK Government Information

VisaPath uses GOV.UK information as its reference source.

Useful official sources include:

- UK Visas and Immigration

https://www.gov.uk/browse/visas-immigration

- Skilled Worker visa

https://www.gov.uk/skilled-worker-visa

- Health and Care Worker visa

https://www.gov.uk/health-care-worker-visa

- Youth Mobility Scheme

https://www.gov.uk/youth-mobility

The application should not be treated as the final legal or official authority.

---

# ⚖️ Disclaimer

VisaPath provides general informational guidance about UK immigration.

It does **not** provide legal advice and does not replace a qualified immigration adviser or solicitor.

Immigration rules and requirements can change. Users should verify important or current information using the latest official UK Government guidance.

The RAG system is intended to improve grounding and reduce unsupported responses, but no AI system should be assumed to be error-free.

---

# 🔒 Sanitisation Notice

This repository is intended for demonstration and portfolio purposes.

The original project was developed in a previous company environment. Company-specific information, confidential data, credentials, production configuration, proprietary implementation details, and other sensitive information have been removed or modified.

This is an independent portfolio project inspired by general engineering patterns I have worked with previously.

It does not contain company code, confidential information, credentials, or proprietary implementation details.

---

# 🚀 Quick Start

```
# Start Ollama models
ollama pull llama3.2
ollama pull nomic-embed-text
```

Backend:

```
cd backend

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Frontend:

```
cd frontend

npm install

npm run dev
```

Evaluation:

```
cd backend

python evaluate.py
```

Then open:

```
http://localhost:5173
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

# 📌 Conclusion

VisaPath is a full-stack AI-powered UK immigration information assistant built with **React, FastAPI, LangChain, Chroma, Ollama, and Llama 3.2**.

The project demonstrates the development of a practical RAG-based AI application, including:

```
Retrieval
   ↓
Grounded Generation
   ↓
Source Tracking
   ↓
Faithfulness Evaluation
   ↓
RAG Evaluation
   ↓
Langfuse Observability
```

The current evaluation baseline achieved:

```
20/20 faithfulness score = 1.00

Average RAG score = 0.94

18/20 RAG evaluations = 1.00
```

This provides a measurable baseline for future improvements to retrieval quality, grounding, evaluation, and overall AI reliability.

VisaPath is therefore not only a conversational AI demonstration, but also a practical example of building an **observable, evaluated, locally hosted RAG application**.

