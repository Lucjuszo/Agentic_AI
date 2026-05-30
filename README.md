# 🤖 Agentic Multi-Domain RAG System

A lightweight, local RAG application using an Agentic Routing architecture. Instead of maintaining multiple databases, the project operates on one optimized Qdrant collection with metadata tagging, ensuring resource efficiency while maintaining high precision.

## 🧠 System Architecture

The system uses TinyLlama (via Ollama) as a "Router." The Router analyzes the user's intent and directs the query to a specialized agent:

- 🏎️ F1 Expert (Formula 1 history & stats)
- 🪐 Space Explorer (Astronomy & Physics)
- 🏙️ Tricity Guide (Tricity history & tourism: Gdańsk, Gdynia, Sopot)
- 🎬 Film Critic (Movies & Cinema)

If a query falls outside these domains, the system switches to a General Assistant for standard interaction.

## 🧪 Tests / Example Queries

Below are example test queries and expected outputs for each domain agent.

### 🏎️ F1 Expert

**Q:** Can you describe the rivalry between Alain Prost and Ayrton Senna?

**Expected Behavior:**  
The agent should explain one of Formula 1’s most iconic rivalries, including:

- Their years as teammates at McLaren
- Key incidents (Suzuka 1989 & 1990)
- Differences in driving style and personality
- Their eventual reconciliation before Senna’s death

**Example Response:**
The rivalry between Alain Prost and Ayrton Senna was one of the most intense in Formula 1 history. While teammates at McLaren in 1988–1989, they dominated the sport but developed a fierce personal and professional conflict. Major flashpoints included controversial collisions at Suzuka in 1989 and 1990, which influenced championship outcomes. Prost was known for his calculated approach, while Senna was famous for aggressive speed and risk-taking. Despite tensions, the two eventually reconciled and gained mutual respect.

---

### 🏙️ Tricity Guide

**Q:** What are the best historical places to visit in Gdansk?

**Expected Behavior:**  
The agent should recommend major historical landmarks in Gdańsk.

**Example Response:**

Recommended historical places in Gdańsk include:

- **St. Mary's Church** – one of the world’s largest brick churches
- **Main Town Hall** – historic Gothic-Renaissance landmark
- **Artus Court** – center of merchant life in old Gdańsk
- **Neptune’s Fountain** – iconic city symbol
- **The Crane (Żuraw)** – medieval port crane
- **European Solidarity Centre** – museum of the Solidarity movement
- **Westerplatte** – symbolic beginning of World War II

---

### 🪐 Space Explorer

**Q:** What are the main characteristics of Jupiter?

**Expected Behavior:**  
The agent should provide scientific facts about Jupiter.

**Example Response:**

Jupiter is the largest planet in the Solar System and is classified as a gas giant.

Key characteristics:

- **Diameter:** ~143,000 km
- **Composition:** Mostly hydrogen and helium
- **Moons:** Over 90 known moons, including Io, Europa, Ganymede, and Callisto
- **Storms:** Home to the Great Red Spot
- **Magnetic Field:** Strongest planetary magnetic field in the Solar System
- **Orbit:** Around 11.86 Earth years

---

### 🎬 Film Critic

**Q:** Best 3 films of all time?

**Expected Behavior:**  
The agent should return highly regarded films based on critical consensus or rankings.

**Example Response:**

1. **The Godfather (1972)**
2. **Citizen Kane (1941)**
3. **Seven Samurai (1954)**

The ranking may vary depending on the source (IMDb, Letterboxd, Sight & Sound, Rotten Tomatoes).

---

### 🌐 General Assistant

**Q:** Who is Elon Musk?

**Expected Behavior:**  
If the question falls outside the domain-specific agents, the system should route to the General Assistant.

**Example Response:**

:contentReference[oaicite:0]{index=0} is a businessman and entrepreneur known for companies such as :contentReference[oaicite:1]{index=1}, :contentReference[oaicite:2]{index=2}, and :contentReference[oaicite:3]{index=3}. He also co-founded PayPal and has been influential in electric vehicles, reusable rockets, and AI-related ventures.

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
