from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import json

# Use the absolute path to the JSON file
file_path = "C:/Users/bensa/OneDrive/Bureau/ecommerce-chatbot/data/Ecommerce_FAQ_Chatbot_dataset.json"

# Debug: Print the file path
print("Loading FAQs from:", file_path)

# Load the FAQs from JSON
with open(file_path, "r") as f:
    faqs_data = json.load(f)
    print("FAQs loaded successfully! Number of FAQs:", len(faqs_data["questions"]))
    print("First FAQ:", faqs_data["questions"][0])  # Debug: Print the first FAQ

# Convert JSON to a list of Q&A pairs
faqs = [{"question": item["question"], "answer": item["answer"]} for item in faqs_data["questions"]]

# Initialize the embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Connect to Qdrant
client = QdrantClient(host="localhost", port=6333)

# Create a collection (like a table)
client.recreate_collection(
    collection_name="faqs",
    vectors_config={"size": model.get_sentence_embedding_dimension(), "distance": "Cosine"}
)

# Add FAQs to the database
embeddings = model.encode([faq["question"] for faq in faqs])
client.upsert(
    collection_name="faqs",
    points=[
        {
            "id": idx,
            "vector": embedding.tolist(),
            "payload": {"answer": faq["answer"]}
        } for idx, (faq, embedding) in enumerate(zip(faqs, embeddings))
    ]
)
print("FAQs loaded into Qdrant!")