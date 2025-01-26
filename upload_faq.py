import json
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from sentence_transformers import SentenceTransformer

# Load the FAQ dataset from JSON
with open("data/Ecommerce_FAQ_Chatbot_dataset.json", "r") as f:
    data = json.load(f)

# Extract the 'questions' array
questions = data["questions"]

# Initialize Qdrant client
client = QdrantClient(host="localhost", port=6333)

# Create the collection if it doesn't exist
collection_name = "faq"
if not client.collection_exists(collection_name):
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)
    )
    print(f"Collection '{collection_name}' created.")
else:
    print(f"Collection '{collection_name}' already exists.")

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings for FAQs
embeddings = model.encode([q["question"] for q in questions])

# Upload data to Qdrant
points = [
    PointStruct(
        id=idx,
        vector=embedding.tolist(),
        payload={"question": q["question"], "answer": q["answer"]}
    )
    for idx, (embedding, q) in enumerate(zip(embeddings, questions))
]

client.upsert(collection_name=collection_name, points=points)
print("FAQ data uploaded to Qdrant!")