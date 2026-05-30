# 🤖 Agentic Multi-Domain RAG System

A fully local, modular command-line application built on an **Agentic Retrieval-Augmented Generation (RAG)** architecture. The system dynamically routes user queries to specialized domain agents using a lightweight local LLM router.

Instead of maintaining multiple vector databases, the application uses a **single optimized Qdrant collection with metadata tagging**, ensuring both resource efficiency and retrieval precision.

The primary goal of the project is to demonstrate **multi-domain knowledge retrieval with intelligent agent routing**, while maintaining a **fully local, privacy-focused architecture** with zero dependency on paid cloud APIs.

---

## 🤖 Supported Agents (Knowledge Domains)

| Agent | Domain |
|---|---|
| 🏎️ **F1 Expert** | Formula 1 history, drivers, rivalries, race statistics |
| 🪐 **Space Explorer** | Astronomy, planets, astrophysics, and space science |
| 🏙️ **Tricity Guide** | History, landmarks, and tourism of Gdańsk, Gdynia, and Sopot |
| 🎬 **Film Critic** | Movies, cinema history, rankings, and recommendations |
| 🌐 **General Assistant** | Fallback agent for general knowledge outside supported domains |

---

##🧪 Tests
🏎️ F1 Expert

Q: Can you describe the rivalry between Alain Prost and Ayrton Senna?

The rivalry between Alain Prost and Ayrton Senna was one of the most intense and memorable in Formula 1 history. Both drivers were extremely talented and competitive, which led to a series of on-track incidents, controversies, and personal clashes.

The tension between them began to build from the late 1980s, with both drivers dominating the sport and seeking to outdo each other. The rivalry was fueled by Prost's perception that McLaren-Honda was giving Senna preferential treatment, which led him to accuse Honda of favoritism towards Senna. This accusation sparked a heated feud between Prost and Senna.

The on-track incidents between them were numerous and infamous. One notable example was at the 1989 Imola Grand Prix, where Prost accused Senna of threatening to sideswipe him into the pit wall during a passing maneuver. Another incident occurred at the 1988 Estoril Grand Prix, where Senna tried to prevent Prost from passing him by making a threat.

The rivalry also extended beyond the track. The two drivers' personal relationships were strained, with Senna reportedly feeling motivated by his rivalry with Prost. In fact, after Prost retired in 1993, Senna admitted that he had relied heavily on their rivalry to fuel his own motivation.

However, despite the intense rivalry, both drivers showed flashes of respect and admiration for each other's abilities. After Senna's death in 1994, both drivers publicly expressed their regret and sadness over the rivalry they had. The rivalry between Alain Prost and Ayrton Senna remains one of the most fascinating and complex in Formula 1 history, with a legacy that continues to captivate fans to this day.

🏙️ Tricity Guide

Q: What are the best historical places to visit in Gdansk?

Gdańsk has a rich history, and there are many historical places to visit in the city. Here are some of the top recommendations:

St. Dominic's Fair: This historic fair dates back to 1260 and is considered one of the biggest trade and cultural events in Europe.

Main City Hall (Ratusz Gdański): A beautiful example of Brick Gothic architecture from the 15th century, it was built on the site of a 13th-century monastery.

Artus Court: A magnificent Renaissance-style palace that now serves as a museum, featuring an impressive collection of art and historical artifacts.

Neptune's Fountain (Fontanna Neptuna): A beautiful fountain located in front of the Town Hall, built by Italian architect Antonio Cibotti in 1733.

The Crane: Also known as the Gdańsk Crane Monument, it's a historic crane that was used to lift heavy weights during the construction of the city's harbor.

Uphagen House (Dom Uphagena): A beautiful example of Brick Gothic architecture from the 15th century, now serving as a museum.

St. Mary's Church (Kościół Mariacki): One of the most iconic landmarks in Gdańsk, this church dates back to the 14th century and features an impressive Gothic interior.

🪐 Space Explorer

Q: What are the main characteristics of Jupiter?

Jupiter's main characteristics are:

Size: Jupiter is the largest planet in our Solar System, with a diameter 11 times that of Earth.

Mass: Jupiter has a mass nearly 2.5 times that of all the other planets combined and slightly less than one-thousandth the mass of the Sun.

Orbital characteristics:

Orbital period: approximately 11.86 years (sidereal) or 398.88 days (synodic).

Distance from Sun: about 5.20 AU (778.5 km).

Atmospheric composition: Primarily composed of hydrogen (76%) and helium (24%) by mass, with traces of elements like carbon, oxygen, sulfur, neon, and compounds such as ammonia, water vapour, phosphine, and hydrocarbons.

Internal structure: Believed to consist of an outer mantle of fluid metallic hydrogen and a diffuse inner core of denser material.

Shape: Due to its rapid rotation rate, Jupiter has an oblate spheroid shape, with the radius to the equator being about 7% larger than the radius to its poles.

Storms and turbulence: Jupiter's outer atmosphere features latitudinal bands with turbulence and storms, including the famous Great Red Spot storm that has been observed since 1831.

🎬 Film Critic

Q: Best 3 films of all time?

Based on the available rankings:

Die Hard (1988)

Aliens (1986)

Seven Samurai (1954)

🌐 General Assistant

Q: Who is Elon Musk?

Elon Musk is a South African-born entrepreneur, inventor, and business magnate. He's best known for revolutionizing the electric car industry with Tesla, SpaceX, and other innovative ventures.

Musk has been a trailblazer in many ways. He co-founded PayPal, SpaceX, Tesla, Neuralink, and The Boring Company. He is also known for his vision, creativity, and passion for making a positive impact on the world.

---

## 🛠️ Tech Stack & Architecture

| Component | Technology |
|---|---|
| **LLM** | `Llama3.2` (locally via Ollama) |
| **Agent Framework** | `agno` |
| **Vector Database** | `Qdrant` (single shared collection, Dockerized) |
| **Embedding Model** | `sentence-transformers/all-MiniLM-L6-v2` |
| **Data Processing** | `LangChain` (chunking), `PyMuPDF` (PDF parsing) |
| **CLI Interface** | `Rich` |

---

## 🚀 Setup & Installation (WSL / Linux)

Follow these steps to recreate the project locally on your machine.

### Step 1: Project Setup & Virtual Environment (`.venv`)

First, open your WSL terminal, create a new directory for the project, and navigate into it.

```bash
# Create the main folder and navigate into it
mkdir f1-rag-project
cd f1-rag-project
```

Next, create a Python Virtual Environment. In the Python ecosystem, installing dependencies globally is considered bad practice, as it leads to version conflicts between different projects. We isolate our project's libraries using `.venv`.

```bash
# Create a virtual environment named '.venv'
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate
```

> You should now see `(.venv)` at the beginning of your terminal prompt, indicating that isolation is active.

### Step 2: Install Dependencies

Install the required libraries directly (no `requirements.txt` needed):

```bash
pip install agno qdrant-client sentence-transformers langchain-text-splitters PyMuPDF rich ollama
```

### Step 3: Start Qdrant Database

```bash
docker-compose up -d
```

### Step 4: Populate the Data Directory (PDFs)

Create the data folder and move your downloaded Wikipedia PDF articles into it.

```bash
# Create the data directory
mkdir -p data/pdfs

# Copy your downloaded PDFs into the project directory
# (Replace '/path/' with the actual path to your PDF files)
cp /path/*.pdf data/pdfs/
```

### Step 5: Run Ingestion Pipeline

Generate embeddings and upload vectors to the shared Qdrant collection:

```bash
python src/ingest.py
```

### Step 6: Launch the System

```bash
python src/cli.py
```

---

## ⚙️ Configuration

Main domain routing rules are defined in `config.py`. The system automatically detects the domain based on the filename of the PDF (e.g., files containing `"Gdansk"` or `"Sopot"` are automatically routed to the Tricity agent).

---

## ⚖️ Data Source & Licensing

**Data Copyright:**
The PDF documents in the `data/` directory are generated from Wikipedia.

**Data License:**
Distributed under the Creative Commons Attribution-ShareAlike License (CC BY-SA 3.0).
