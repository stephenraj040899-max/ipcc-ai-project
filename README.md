# 🌍 IPCC Climate AI Assistant

An AI-powered climate knowledge assistant built using **Google Cloud Platform**, **Vertex AI**, **BigQuery Vector Search**, **Gemini**, and **Streamlit**.

The application allows users to ask questions about the **IPCC Special Report on Cities**, retrieve relevant document passages using semantic search, and generate AI-powered answers with citations.

---

## 🚀 Live Demo

Cloud Run URL:

https://ipcc-ai-project-510679909889.us-central1.run.app

---

# Features

### 🤖 AI Question Answering
- Ask questions in natural language
- Semantic retrieval using BigQuery Vector Search
- AI-generated answers using Gemini
- Displays document sources used for every answer

---

### 📚 Browse Documents

- Browse all IPCC reports stored in Google Cloud Storage
- Download original PDF documents
- Preview document information

---

### 📄 Document Summary

Generate concise summaries for any uploaded IPCC report.

---

### 📝 Document Review

Generate an AI review including:

- Key findings
- Strengths
- Weaknesses
- Overall assessment

---

### 💡 Improvement Suggestions

Receive AI-generated recommendations for improving documents.

---

### 💬 Chat Interface

- Conversation history
- Multiple questions
- Source citations
- Clean Streamlit interface

---

# Architecture

```
                User
                  │
                  ▼
          Streamlit UI
                  │
                  ▼
          Gemini 2.5 Flash
                  │
        Retrieval Service
                  │
                  ▼
       BigQuery Vector Search
                  │
                  ▼
        Vertex AI Embeddings
                  │
                  ▼
        IPCC Document Chunks
                  │
                  ▼
         Google Cloud Storage
```

---

# Tech Stack

## Frontend

- Streamlit

## Backend

- Python
- Vertex AI
- Gemini 2.5 Flash
- BigQuery
- BigQuery Vector Search
- Google Cloud Storage

## AI

- Gemini 2.5 Flash
- text-embedding-005

## Cloud

- Google Cloud Run
- Docker
- Cloud Build

---

# Project Structure

```
ipcc-ai-project/

├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── README.md

├── prompts/
│
├── scripts/
│
├── services/
│   ├── bigquery_service.py
│   ├── chunker.py
│   ├── document_service.py
│   ├── embedding_service.py
│   ├── improvement_service.py
│   ├── llm_service.py
│   ├── pdf_processor.py
│   ├── prompt_loader.py
│   ├── retrieval_service.py
│   ├── review_service.py
│   ├── storage.py
│   ├── summary_service.py
│   └── vector_search.py
│
├── tests/
│
├── ui/
│   └── streamlit_app.py
│
└── docs/
```

---

# Workflow

1. Upload PDFs to Google Cloud Storage
2. Extract text using PyMuPDF
3. Split text into chunks
4. Store chunks in BigQuery
5. Generate embeddings using Vertex AI
6. Build BigQuery Vector Index
7. User asks a question
8. Generate query embedding
9. Retrieve relevant chunks
10. Gemini generates the final answer

---

# Installation

Clone the repository

```bash
git clone https://github.com/stephenraj040899-max/ipcc-ai-project.git
```

Create a virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
PROJECT_ID=ai-ippc
LOCATION=us-central1

DATASET_ID=climate_ai

DOCUMENTS_TABLE=documents

EMBEDDINGS_TABLE=embeddings

BUCKET_NAME=ipcc-srcities-bucket-1

GEMINI_MODEL=gemini-2.5-flash

EMBEDDING_MODEL=text-embedding-005
```

Run

```bash
streamlit run ui/streamlit_app.py
```

---

# Deployment

The application is containerized using Docker and deployed on Google Cloud Run.

```bash
docker build -t ipcc-ai-project .
```

```bash
gcloud run deploy
```

---

# Future Improvements

- Compare multiple documents
- Export answers to PDF and Word
- Google Gen AI SDK migration
- Authentication
- User history
- Multi-document chat
- Advanced analytics dashboard

---

# Author

**Stephen Raj**

GitHub

https://github.com/stephenraj040899-max

---

# License

MIT License