🤖 AI Assistant using Endee (RAG-based Application)

An AI-powered Assistant built using Retrieval-Augmented Generation (RAG) with Endee as the vector database.
This project demonstrates how to index documents, perform semantic search, and retrieve relevant context for user queries using embeddings.

Project Overview

This project was developed as part of an AI/ML interview assignment to demonstrate:

  * Vector database usage (Endee)
  * Semantic search & RAG workflow
  * Embedding generation using Sentence Transformers
  * Interactive UI using Streamlit
  * Cloud deployment on Streamlit Cloud

🚀 Key Features

 * 🔍 Semantic Search using vector embeddings
 * 🧠 RAG Architecture (Retrieve → Use context)
 * 📦 Endee Vector Database for storage & querying
 * 🖥️ Streamlit UI for interactive querying
 * ☁️ Cloud Deployment Ready
 * 🧩 Modular, clean codebase (easy to extend)

 Architecture (High Level)

              User Query
                  ↓
      SentenceTransformer (Embeddings)
                  ↓
        Endee Vector Database (Query)
                  ↓
           Relevant Documents
                  ↓
          Displayed in Streamlit UI

Project Structure
            
    ai-assistant-rag/
    │
    ├── app.py                # Streamlit app entry point
    ├── embedder.py           # Embedding logic using SentenceTransformer
    ├── endee_store.py        # Endee vector DB wrapper
    ├── retriever.py          # Retrieval abstraction
    ├── documents.txt         # Sample knowledge base
    ├── requirements.txt      # Python dependencies
    ├── README.md             # Project documentation
    └── .gitignore

Tech Stack

  * Python 3.10+
  * Endee (Vector Database)
  * Sentence-Transformers
  * Streamlit
  * Git & GitHub
  * Streamlit Cloud (Deployment)

Installation & Setup (Local)
  * Clone Repository

         git clone https://github.com/VivekChowdary9/ai-assistant-rag.git cd ai-assistant-rag

  * Create Virtual Environment

            python -m venv venv
  *  Activate Virtual Environment

              venv\Scripts\activate
  * Install Dependencies

               pip install -r requirements.txt
  *  Run the Application

               streamlit run app.py

Streamlit Cloud Deployment

  * Push code to GitHub
  * Go to 👉 https://share.streamlit.io
  * Click New App
  * Select:
         Repository: ai-assistant-rag
         Branch: main
         Main file: app.py
  * Click Deploy

How Endee is Used

 * Endee stores vector embeddings
 * Collections are explicitly created
 * Querying is done via vector similarity

          db = Endee()
          db.create_collection("documents")
          db.add(...)
          db.query(...)

Output 

<img width="1915" height="967" alt="Screenshot 2026-02-03 101055" src="https://github.com/user-attachments/assets/1ed5c067-f45d-4836-a732-8c572c2bca26" />
<img width="1916" height="975" alt="Screenshot 2026-02-03 101331" src="https://github.com/user-attachments/assets/b2529ffe-acd4-4670-82fd-c65e0ab76702" />

Streamlit Link : https://ai-assistant-rag-kuwufuyg52hc37pnb4yd6l.streamlit.app/

Future Enhancements

  * ChatGPT / LLM-based answer generation
  * File upload (PDF, DOCX, TXT)
  * Conversation memory
  * Source citation
  * Authentication

Author
   * Vivek Chowdary Namburi
   * CSE Department – SRM AP University
   * GitHub: https://github.com/VivekChowdary9
