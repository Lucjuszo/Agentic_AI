from agno.agent import Agent
from agno.models.ollama import Ollama
from retriever import Retriever

retriever = Retriever()

def get_model():
    return Ollama(id="llama3.2")

def build_context(hits: list[dict]):
    return "\n\n".join(
        f"[{h['label']} | score {h['score']}]\n{h['text']}" for h in hits
    )

def make_f1_agent():
    return Agent(
        name="F1 Expert",
        model=get_model(),
        instructions="""You are a Formula 1 historian and analyst.
Answer only from the provided context. Be precise about seasons, lap times,
championships, and rivalries. If context is insufficient, say so clearly.
Never invent statistics.""",
    )

def make_cosmos_agent():
    return Agent(
        name="Space Explorer",
        model=get_model(),
        instructions="""You are an astrophysicist and space science communicator.
Answer only from the provided context about planets, the solar system,
and space phenomena. Use scientific accuracy. If context is insufficient,
say so clearly.""",
    )

def make_tricity_agent():
    return Agent(
        name="Tricity Guide",
        model=get_model(),
        instructions="""You are a local expert guide for the Tricity area
(Gdańsk, Gdynia, Sopot) in Poland. Answer only from the provided context.
Recommend attractions, history, food, and local tips. If context is
insufficient, say so clearly.""",
    )

def make_film_agent():
    return Agent(
        name="Film Critic",
        model=get_model(),
        instructions="""You are a knowledgeable film critic and cinema historian.
Answer only from the provided context about movies, directors, actors,
and film history. If context is insufficient, say so clearly.""",
    )

_INTENT_INSTRUCTIONS = """You are a routing assistant. Your ONLY job is to classify
the user's query into exactly one of these domains:
  f1       - Formula 1 racing, drivers, seasons, races
  cosmos   - space, planets, solar system, astronomy
  tricity  - Gdańsk, Gdynia, Sopot, Tricity region Poland
  film     - movies, cinema, directors, actors
  other    - casual conversation, jokes, general knowledge, greetings

Reply with ONLY the domain keyword, nothing else.
Examples:
  "Who won the 1994 championship?" → f1
  "How big is Jupiter?" → cosmos
  "What to see in Sopot?" → tricity
  "Best Kubrick films?" → film
  "Tell me a joke about AI" → other"""

def make_root_agent():
    return Agent(
        name="Root Router",
        model=get_model(),
        instructions=_INTENT_INSTRUCTIONS,
    )

SPECIALIST = {
    "f1":      make_f1_agent,
    "cosmos":  make_cosmos_agent,
    "tricity": make_tricity_agent,
    "film":    make_film_agent,
}

DOMAIN_LABELS = {
    "f1":      "F1 Expert",
    "cosmos":  "Space Explorer",
    "tricity": "Tricity Guide",
    "film":    "Film Critic",
}


class MultiAgentSystem:
    def __init__(self):
        self.root = make_root_agent()
        self._agents: dict[str, Agent] = {}

    def _get_agent(self, domain: str):
        if domain not in self._agents:
            self._agents[domain] = SPECIALIST[domain]()
        return self._agents[domain]

    def run(self, query: str):
        """Returns (domain, answer)."""
        # 1. Detect intent
        intent_resp = self.root.run(query)
        domain = intent_resp.content.strip().lower()

        # 2. General conversation fallback
        if domain not in SPECIALIST:
            general_agent = Agent(
                name="General Assistant",
                model=get_model(),
                instructions="You are a friendly AI. Engage in casual conversation and tell jokes. Answer in English."
            )
            answer = general_agent.run(query)
            return "General Assistant", answer.content.strip()

        # 3. Retrieve relevant chunks (tylko dla specjalistów)
        hits = retriever.search(query, domain=domain)
        if not hits:
            return domain, "I couldn't find relevant information in my knowledge base."

        context = build_context(hits)

        # 4. Ask specialist agent
        prompt = f"Context from knowledge base:\n{context}\n\nQuestion: {query}"
        agent  = self._get_agent(domain)
        answer = agent.run(prompt)

        return domain, answer.content.strip()