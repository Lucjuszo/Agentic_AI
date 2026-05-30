import uuid
from pathlib import Path
import fitz
from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
from rich.console import Console
from rich.progress import track

from config import (QDRANT_URL, COLLECTION_NAME, EMBEDDING_MODEL,
                    VECTOR_SIZE, CHUNK_SIZE, CHUNK_OVERLAP, DOMAIN_RULES)

PDFS_DIR = Path(__file__).parent.parent / "data" / "pdfs"
console  = Console()

def detect_domain(filename: str):
    stem = Path(filename).stem
    for domain, keywords in DOMAIN_RULES:
        if any(kw.lower() in stem.lower() for kw in keywords):
            return domain
    return "general"

def extract_text(pdf_path: Path):
    doc = fitz.open(pdf_path)
    return "\n".join(page.get_text() for page in doc)

def load_pdfs(pdfs_dir: Path):
    docs = []
    for path in sorted(pdfs_dir.glob("*.pdf")):
        text   = extract_text(path)
        domain = detect_domain(path.name)
        label  = path.stem.replace("_", " ")
        docs.append({"filename": path.name, "label": label,
                     "domain": domain, "text": text})
        console.print(f"  [green]✓[/green] [{domain:8s}] {label} ({len(text):,} chars)")
    return docs

def chunk_docs(docs: list[dict]):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = []
    for doc in docs:
        for i, part in enumerate(splitter.split_text(doc["text"])):
            chunks.append({
                "id":      str(uuid.uuid4()),
                "text":    part,
                "label":   doc["label"],
                "domain":  doc["domain"],
                "source":  doc["filename"],
                "chunk_i": i,
            })
    return chunks


def setup_collection(client: QdrantClient):
    names = [c.name for c in client.get_collections().collections]
    if COLLECTION_NAME in names:
        console.print(f"Dropping existing '{COLLECTION_NAME}'")
        client.delete_collection(COLLECTION_NAME)
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
    )
    console.print(f"Collection '{COLLECTION_NAME}' created.")


def embed_and_upload(chunks: list[dict], client: QdrantClient,
                     model: SentenceTransformer):
    texts   = [c["text"] for c in chunks]
    console.print("\n[bold]Generating embeddings…[/bold]")
    vectors = model.encode(texts, show_progress_bar=True, batch_size=32)

    points = [
        PointStruct(
            id=c["id"], vector=v.tolist(),
            payload={"text": c["text"], "label": c["label"],
                     "domain": c["domain"], "source": c["source"],
                     "chunk_i": c["chunk_i"]},
        )
        for c, v in zip(chunks, vectors)
    ]

    bs = 128
    for i in track(range(0, len(points), bs), description="Uploading…"):
        client.upsert(collection_name=COLLECTION_NAME, points=points[i:i+bs])
    console.print(f"[green]✓[/green] Uploaded {len(points)} chunks.")


def main():
    console.rule("[bold blue]Agentic RAG – Ingest Pipeline[/bold blue]")

    console.print("\n[bold]1. Loading PDFs…[/bold]")
    docs = load_pdfs(PDFS_DIR)
    if not docs:
        console.print("[red]No PDFs found![/red]"); return

    console.print(f"\n[bold]2. Chunking…[/bold]")
    chunks = chunk_docs(docs)
    console.print(f"   Total chunks: [cyan]{len(chunks)}[/cyan]")

    # domain breakdown
    from collections import Counter
    for domain, count in Counter(c["domain"] for c in chunks).items():
        console.print(f"   {domain:10s}: {count} chunks")

    console.print(f"\n[bold]3. Loading embedding model…[/bold]")
    model = SentenceTransformer(EMBEDDING_MODEL)

    console.print(f"\n[bold]4. Connecting to Qdrant…[/bold]")
    client = QdrantClient(url=QDRANT_URL)
    setup_collection(client)

    console.print(f"\n[bold]5. Embed & upload…[/bold]")
    embed_and_upload(chunks, client, model)

    console.rule("[bold green]Ingest complete![/bold green]")


if __name__ == "__main__":
    main()