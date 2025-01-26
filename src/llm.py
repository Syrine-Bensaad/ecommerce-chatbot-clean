from transformers import pipeline
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def generate_response(query, context):
    prompt = f"""
    You are a professional ecommerce assistant. Answer the user's question using ONLY the context below. 
    If the answer isn't in the context, say: "I can't help with that. Contact support@example.com."

    Context: {context}

    Question: {query}

    Answer:
    """
    # Load a pre-trained model from Hugging Face
    generator = pipeline("text-generation", model="gpt2")
    response = generator(prompt, max_length=100, num_return_sequences=1)
    return response[0]['generated_text'].strip()

if __name__ == "__main__":
    query = "How do I contact support?"
    context = ["Our support email is support@example.com."]
    response = generate_response(query, context)
    print("LLM Response:")
    print(response)