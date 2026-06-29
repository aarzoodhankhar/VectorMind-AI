# 🚀 VectorMind

> **Private AI Knowledge Engine built in C++ using Vector Search, Retrieval-Augmented Generation (RAG), and Local LLMs.**

VectorMind is a local AI-powered knowledge engine that allows users to upload documents, extract knowledge from PDFs, perform semantic search using vector embeddings, and ask natural language questions through a Retrieval-Augmented Generation (RAG) pipeline—all without relying on paid cloud APIs.

---

# ✨ Features

* 🔍 Semantic Vector Search
* 📄 PDF Text Extraction & Ingestion
* 🧠 Retrieval-Augmented Generation (RAG)
* 🤖 Local AI using Ollama
* 📚 Persistent Knowledge Base
* ⚡ HNSW, KD-Tree & Brute Force Search
* 📊 Interactive Vector Space Visualization
* 💬 AI Chat over Uploaded Documents
* 💾 Local Storage (No Cloud Required)

---

# 🏗 Architecture

```text
                PDF / Text
                     │
                     ▼
            Text Extraction
                     │
                     ▼
             Document Chunking
                     │
                     ▼
        Ollama Embedding Model
         (nomic-embed-text)
                     │
                     ▼
             Vector Database
          (HNSW / KD-Tree)
                     │
                     ▼
          Semantic Retrieval
                     │
                     ▼
      Local LLM (llama3.2 via Ollama)
                     │
                     ▼
            AI Generated Answer
```

---

# 🚀 Tech Stack

| Category       | Technologies               |
| -------------- | -------------------------- |
| Language       | C++17                      |
| Backend        | cpp-httplib                |
| Frontend       | HTML, CSS, JavaScript      |
| PDF Processing | Python, pypdf              |
| Embeddings     | Ollama (nomic-embed-text)  |
| LLM            | Ollama (llama3.2)          |
| Search         | HNSW, KD-Tree, Brute Force |
| Storage        | Local Persistent Storage   |

---

# 🖥 Application Modules

### 🔹 Vector Search

* Semantic similarity search
* Multiple search algorithms
* PCA visualization
* Search latency benchmarking

### 🔹 Knowledge Base

* Add custom text
* Index PDF documents
* Automatic chunking
* Persistent storage

### 🔹 AI Assistant

* Retrieval-Augmented Generation (RAG)
* Context-aware answers
* Local inference using Ollama
* Interactive conversation interface

---

# 📸 Screenshots

> Add screenshots here.

Example:

```
screenshots/search.png
screenshots/knowledge-base.png
screenshots/assistant.png
```

---

# 📂 Project Structure

```
VectorMind/
│
├── main.cpp
├── index.html
├── extract_pdf.py
├── documents.txt
├── httplib.h
├── README.md
└── screenshots/
```

---

# ⚙️ Getting Started

## Clone Repository

```bash
git clone https://github.com/aarzoodhankhar/VectorMind-AI.git
cd VectorMind-AI
```

## Install Python Dependency

```bash
pip install pypdf
```

## Install Ollama

Install Ollama and download the required models:

```bash
ollama pull nomic-embed-text
ollama pull llama3.2
```

## Build

Using MSYS2 UCRT64:

```bash
g++ -std=c++17 -O2 main.cpp -o db.exe -lws2_32
```

## Run

```bash
./db.exe
```

Open:

```
http://localhost:8080
```

---

# 💡 How It Works

1. Upload a PDF or add custom text.
2. The document is split into semantic chunks.
3. Ollama generates vector embeddings.
4. Embeddings are stored inside the vector database.
5. User asks a question.
6. Most relevant chunks are retrieved.
7. The local LLM generates an answer using retrieved context.

---

# 🔮 Future Improvements

* Drag & Drop PDF Upload
* Multiple File Upload
* Image OCR Support
* Hybrid Search (Keyword + Vector)
* Conversation Memory
* Metadata Filtering
* Authentication
* Export & Import Knowledge Bases

---

# 📈 Resume Highlights

* Developed a C++-based Vector Database supporting semantic search and Retrieval-Augmented Generation (RAG).
* Implemented PDF ingestion, document chunking, and local embedding generation using Ollama.
* Built an interactive web interface for document indexing, semantic retrieval, and AI-powered question answering.
* Designed a local-first architecture with HNSW indexing, persistent storage, and real-time vector visualization.

---

# 👩‍💻 Author

**Aarzoo Dhankhar**

B.Tech Information Technology | IGDTUW

GitHub: https://github.com/aarzoodhankhar

---

⭐ If you found this project interesting, consider giving it a star!
