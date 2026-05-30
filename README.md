# 🤖 Agentic Multi-Domain RAG System

A lightweight, local RAG application using an Agentic Routing architecture. Instead of maintaining multiple databases, the project operates on one optimized Qdrant collection with metadata tagging, ensuring resource efficiency while maintaining high precision.

## 🧠 System Architecture

The system uses TinyLlama (via Ollama) as a "Router." The Router analyzes the user's intent and directs the query to a specialized agent:

- 🏎️ F1 Expert (Formula 1 history & stats)
- 🪐 Space Explorer (Astronomy & Physics)
- 🏙️ Tricity Guide (Tricity history & tourism: Gdańsk, Gdynia, Sopot)
- 🎬 Film Critic (Movies & Cinema)

If a query falls outside these domains, the system switches to a General Assistant for standard interaction.

## 🧪 Tests

### 🏎️ F1 Expert

**Q:** Can you describe the rivalry between Alain Prost and Ayrton Senna?

The rivalry between Alain Prost and Ayrton Senna was one of the most intense and memorable in Formula 1 history. Both drivers were extremely talented and competitive, which led to a series of on-track incidents, controversies, and personal clashes.

The tension between them began to build from the late 1980s, with both drivers dominating the sport and seeking to outdo each other. The rivalry was fueled by Prost's perception that McLaren-Honda was giving Senna preferential treatment, which led him to accuse Honda of favoritism towards Senna. This accusation sparked a heated feud between Prost and Senna.

The on-track incidents between them were numerous and infamous. One notable example was at the 1989 Imola Grand Prix, where Prost accused Senna of threatening to sideswipe him into the pit wall during a passing maneuver. Another incident occurred at the 1988 Estoril Grand Prix, where Senna tried to prevent Prost from passing him by making a threat.

The rivalry also extended beyond the track. The two drivers' personal relationships were strained, with Senna reportedly feeling motivated by his rivalry with Prost. In fact, after Prost retired in 1993, Senna admitted that he had relied heavily on their rivalry to fuel his own motivation.

However, despite the intense rivalry, both drivers showed flashes of respect and admiration for each other's abilities. After Senna's death in 1994, both drivers publicly expressed their regret and sadness over the rivalry they had. The rivalry between Alain Prost and Ayrton Senna remains one of the most fascinating and complex in Formula 1 history, with a legacy that continues to captivate fans to this day.

### 🏙️ Tricity Guide

**Q:** What are the best historical places to visit in Gdansk?

Gdańsk has a rich history, and there are many historical places to visit in the city. Here are some of the top recommendations:

St. Dominic's Fair: This historic fair dates back to 1260 and is considered one of the biggest trade and cultural events in Europe.

Main City Hall (Ratusz Gdański): A beautiful example of Brick Gothic architecture from the 15th century, it was built on the site of a 13th-century monastery.

Artus Court: A magnificent Renaissance-style palace that now serves as a museum, featuring an impressive collection of art and historical artifacts.

Neptune's Fountain (Fontanna Neptuna): A beautiful fountain located in front of the Town Hall, built by Italian architect Antonio Cibotti in 1733.

The Crane: Also known as the Gdańsk Crane Monument, it's a historic crane that was used to lift heavy weights during the construction of the city's harbor.

Uphagen House (Dom Uphagena): A beautiful example of Brick Gothic architecture from the 15th century, now serving as a museum.

St. Mary's Church (Kościół Mariacki): One of the most iconic landmarks in Gdańsk, this church dates back to the 14th century and features an impressive Gothic interior.

### 🪐 Space Explorer

**Q:** What are the main characteristics of Jupiter?

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

### 🎬 Film Critic

**Q:** Best 3 films of all time?

Based on the available rankings:

Die Hard (1988)

Aliens (1986)

Seven Samurai (1954)

### 🌐 General Assistant

**Q:** Who is Elon Musk?

Elon Musk is a South African-born entrepreneur, inventor, and business magnate. He's best known for revolutionizing the electric car industry with Tesla, SpaceX, and other innovative ventures.

Musk has been a trailblazer in many ways. He co-founded PayPal, SpaceX, Tesla, Neuralink, and The Boring Company. He is also known for his vision, creativity, and passion for making a positive impact on the world.

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
