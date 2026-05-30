# 🤖 Agentic Multi-Domain RAG System

A lightweight, local RAG application using an Agentic Routing architecture. Instead of maintaining multiple databases, the project operates on one optimized Qdrant collection with metadata tagging, ensuring resource efficiency while maintaining high precision.

## 🧠 System Architecture

The system uses TinyLlama (via Ollama) as a "Router." The Router analyzes the user's intent and directs the query to a specialized agent:

- 🏎️ F1 Expert (Formula 1 history & stats)
- 🪐 Space Explorer (Astronomy & Physics)
- 🏙️ Tricity Guide (Tricity history & tourism: Gdańsk, Gdynia, Sopot)
- 🎬 Film Critic (Movies & Cinema)

If a query falls outside these domains, the system switches to a General Assistant for standard interaction.

## 🛠️ Tech Stack

- **LLM:** TinyLlama-1.1B-Chat-v1.0 (locally via Ollama)
- **Agent Framework:** agno (for agent orchestration)
- **Vector Database:** Qdrant (Dockerized)
- **Embedding Model:** sentence-transformers/all-MiniLM-L6-v2
- **Data Processing:** LangChain (chunking), PyMuPDF (PDF parsing)
- **CLI Interface:** Rich

## 🚀 Installation & Setup

### Environment Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install agno qdrant-client sentence-transformers langchain-text-splitters PyMuPDF rich
```

### Start the Vector Database

```bash
docker-compose up -d
```

### Data Ingestion

Place your PDFs in the `data/pdfs/` folder and run the indexing process:

```bash
python src/ingest.py
```

### Launch System

```bash
python src/cli.py
```
