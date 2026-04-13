from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from dotenv import load_dotenv
import os
import time

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# ── Load & chunk data ─────────────────────────────────────────
extracted_data = load_pdf_file(data='Data/')
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

# ── Pinecone setup ────────────────────────────────────────────
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medicalbot"

# ── Delete index if it already exists ────────────────────────
if index_name in pc.list_indexes().names():
    print(f"Deleting existing index '{index_name}'...")
    pc.delete_index(index_name)
    time.sleep(5)

# ── Create fresh index ────────────────────────────────────────
print(f"Creating index '{index_name}'...")
pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1")
)

# ── Wait until ready ──────────────────────────────────────────
print("Waiting for index to be ready...")
while not pc.describe_index(index_name).status['ready']:
    print("  ...still initializing")
    time.sleep(3)
print("Index is ready!")

# ── Get the index and upsert embeddings directly ──────────────
index = pc.Index(index_name)

print(f"Uploading {len(text_chunks)} chunks...")

# Embed and upsert in batches of 100
batch_size = 100
for i in range(0, len(text_chunks), batch_size):
    batch = text_chunks[i:i + batch_size]
    texts = [doc.page_content for doc in batch]
    vectors = embeddings.embed_documents(texts)
    upserts = [
        (
            f"chunk-{i + j}",
            vectors[j],
            {"text": texts[j], "source": batch[j].metadata.get("source", "")}
        )
        for j in range(len(batch))
    ]
    index.upsert(vectors=upserts)
    print(f"  Uploaded batch {i // batch_size + 1} / {(len(text_chunks) - 1) // batch_size + 1}")

print(f" Done! {len(text_chunks)} chunks uploaded to '{index_name}'.")
print(index.describe_index_stats())