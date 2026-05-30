QDRANT_URL      = "http://localhost:6333"
COLLECTION_NAME = "agents_knowledge"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTOR_SIZE     = 384

CHUNK_SIZE      = 900
CHUNK_OVERLAP   = 120

TOP_K           = 3

# domain tag per filename pattern
DOMAIN_RULES = [
    ("f1",      ["Prost", "Senna", "Alonso", "Hamilton", "Verstappen",
                 "Schumacher", "Raikkonen", "Rosberg", "Lauda", "Vettel",
                 "Stewart", "Fangio"]),
    ("cosmos",  ["cosmos", "earth", "jupiter", "mars", "mercury",
                 "neptune", "pluto", "saturn", "solarsystem",
                 "sun", "uranus", "venus"]),
    ("tricity", ["Gdansk", "Gdynia", "Sopot", "tricity"]),
    ("film",    ["film"]),
]