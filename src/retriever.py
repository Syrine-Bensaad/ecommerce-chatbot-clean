from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
client = QdrantClient(host="localhost", port=6333)

def search_faq(query, top_k=3):
    query_embedding = model.encode(query).tolist()
    results = client.search(
        collection_name="faqs",
        query_vector=query_embedding,
        limit=top_k
    )
    return [{"answer": hit.payload["answer"], "score": hit.score} for hit in results] 