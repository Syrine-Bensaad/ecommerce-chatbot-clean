# app.py (updated)
from flask import Flask, request, jsonify
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

app = Flask(__name__)
model = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient(host="qdrant", port=6333)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get('query', '')
    
    # Generate embedding for the query
    query_embedding = model.encode(query).tolist()
    
    # Search Qdrant
    results = client.search(
        collection_name="faq",
        query_vector=query_embedding,
        limit=1
    )
    
    if results:
        return jsonify({"response": results[0].payload["answer"]})
    return jsonify({"response": "Sorry, I don't understand that question."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)