# Ecommerce Chatbot with RAG System

This project implements a chatbot for an ecommerce platform using a **Retrieval-Augmented Generation (RAG)** system. The chatbot retrieves relevant FAQ entries from a vector database (Qdrant) and provides accurate, professional, and user-friendly responses.

---

## Features
- **Vector Database Integration**: Uses Qdrant to store and retrieve FAQ embeddings.
- **Retrieval Mechanism**: Finds the most relevant FAQ entries based on user queries.
- **Chatbot API**: Built with Flask to handle user queries and return responses.
- **Frontend Interface**: Simple HTML/CSS/JavaScript frontend for user interaction.
- **Dockerized Deployment**: Easy deployment using Docker and Docker Compose.

---

## Installation

### Prerequisites
- Python 3.8+
- Docker
- Docker Compose

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Syrine-Bensaad/ecommerce-chatbot.git
   cd ecommerce-chatbot
   
