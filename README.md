# Ecommerce Chatbot with RAG System

This project implements a chatbot for an ecommerce platform using a **Retrieval-Augmented Generation (RAG)** system. The chatbot retrieves relevant FAQ entries from a vector database (Qdrant) and provides accurate, professional, and user-friendly responses.

---

## Why Use a RAG System?

In the context of an ecommerce platform, a **Retrieval-Augmented Generation (RAG)** system is highly beneficial for the following reasons:

### **Accurate Responses**
The RAG system combines the strengths of retrieval-based and generative models. It retrieves relevant information from a structured FAQ database and uses a Large Language Model (LLM) to generate context-aware responses. This ensures that the chatbot provides accurate and relevant answers to user queries.

### **Efficiency**
By retrieving relevant FAQ entries first, the system reduces the computational load on the LLM, making the chatbot more efficient and cost-effective.

### **Scalability**
The RAG system can easily scale to handle a large number of FAQs and user queries, making it suitable for growing ecommerce platforms.

### **User Experience**
The system ensures that the chatbot maintains a professional and friendly tone, enhancing the overall user experience.

---

## Steps Followed During the Development Process

### **Data Preparation**
- The FAQ dataset was loaded from a JSON file (`Ecommerce_FAQ_Chatbot_dataset.json`).
- The dataset contains a list of questions and answers related to ecommerce operations.

### **Vector Database Integration**
- **Qdrant** was chosen as the vector database to store FAQ embeddings.
- The `upload_faq.py` script was used to generate embeddings for each FAQ question using the `sentence-transformers/all-MiniLM-L6-v2` model and upload them to Qdrant.

### **Retrieval Mechanism**
- The chatbot uses the `sentence-transformers` library to generate embeddings for user queries.
- The query embedding is then used to search the Qdrant database for the most relevant FAQ entry.

### **Chatbot API Development**
- A **Flask-based API** (`app.py`) was developed to handle user queries.
- The API exposes a `/chat` endpoint that accepts user queries, retrieves the most relevant FAQ entry from Qdrant, and returns the answer.

### **Frontend Development**
- A simple **HTML frontend** (`index.html`) was created to allow users to interact with the chatbot.
- The frontend communicates with the Flask API using JavaScript's `fetch` API.

### **Containerization and Deployment**
- The application was containerized using **Docker** and **Docker Compose**.
- Two services were defined in the `docker-compose.yml` file: one for Qdrant and one for the Flask application.

### **Testing and Validation**
- The chatbot was tested with various user queries to ensure accurate retrieval and response generation.
- The system was validated for scalability and performance.

---

## Reasons for Choosing Specific Models and Technologies

### **Qdrant (Vector Database)**
- **Performance**: Qdrant is optimized for high-performance vector similarity search, making it ideal for retrieving relevant FAQ entries.
- **Scalability**: Qdrant can handle large datasets and high query volumes, ensuring the chatbot can scale with the platform.
- **Ease of Use**: Qdrant provides a simple and intuitive API for storing and retrieving vector embeddings.

### **Sentence-Transformers (Embedding Model)**
- **Efficiency**: The `all-MiniLM-L6-v2` model is lightweight and efficient, providing high-quality embeddings for text similarity tasks.
- **Accuracy**: The model is well-suited for generating embeddings for both FAQ questions and user queries, ensuring accurate retrieval.

### **Flask (Web Framework)**
- **Simplicity**: Flask is a lightweight and flexible web framework, making it easy to build and deploy the chatbot API.
- **Scalability**: Flask can be easily extended to handle more complex use cases, such as integrating an LLM for response generation.

### **Docker (Containerization)**
- **Consistency**: Docker ensures consistent environments across development and production, reducing the risk of deployment issues.
- **Ease of Deployment**: Docker Compose simplifies the orchestration of multiple services (e.g., Qdrant and Flask), making deployment straightforward.

---

## Justifications for Selecting Qdrant as the Vector Database

### **High Performance**
Qdrant is optimized for vector similarity search, ensuring fast and accurate retrieval of relevant FAQ entries.

### **Scalability**
Qdrant can handle large datasets and high query volumes, making it suitable for growing ecommerce platforms.

### **Ease of Integration**
Qdrant provides a simple and intuitive API for storing and retrieving vector embeddings, making it easy to integrate with the chatbot.

### **Community and Support**
Qdrant has an active community and comprehensive documentation, ensuring that developers can easily find support and resources.

### **Cost-Effectiveness**
Qdrant is open-source and free to use, making it a cost-effective solution for vector storage and retrieval.

---

## Conclusion
The RAG system implemented in this project provides a robust and scalable solution for building an ecommerce chatbot. By leveraging Qdrant for vector storage and retrieval, and Flask for the chatbot API, the system ensures accurate and efficient responses to user queries. The use of Docker for containerization further simplifies deployment and scaling.

---

## References
- [Qdrant Documentation](https://qdrant.tech/documentation/)
- [Sentence-Transformers Documentation](https://www.sbert.net/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)
