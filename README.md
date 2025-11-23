# 🚀 RAG System with Groq, ChromaDB & Sentence Transformers

A **Retrieval-Augmented Generation (RAG) System** that answers questions from your JSON documents using Groq LLM, ChromaDB vector database, and Sentence Transformers.

## ✨ Features

- ⚡ **Fast**: Groq LLM inference + ChromaDB vector search
- 🔍 **Semantic Search**: Find relevant documents using embeddings
- 💾 **Local Storage**: No cloud dependencies
- 🆓 **Free**: Groq free tier + local embeddings

## 📋 Prerequisites

- Python 3.8+
- Groq API Key (FREE at [console.groq.com](https://console.groq.com/))
- Basic understanding of Python

---

## 🚀 Quick Start Guide

### 🔥 Step 1: Create Groq API Key

1. Go to: https://console.groq.com
2. Sign in (create account if needed)
3. Click **API Keys** → **Create Key**
4. Copy the key starting with `gsk_...`

### 🛠 Step 2: Set Up Project

```bash
# Create project directory
mkdir my-rag-project
cd my-rag-project

# Create virtual environment
python -m venv rag_env

# Activate virtual environment
rag_env\Scripts\activate     # Windows
# source rag_env/bin/activate  # Mac/Linux

# Install required packages
pip install groq chromadb sentence-transformers tiktoken python-dotenv
```

### 🔑 Step 3: Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=gsk_your_api_key_here
```

**Get your FREE Groq API key**: https://console.groq.com/

### 🤖 Step 4: Test LLM Connection

Create `test_llm.py` to verify Groq is working:

```python
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "Hello! Can you hear me?"}]
)

print("✅ LLM Response:", response.choices[0].message.content)
```

**Run it:**
```bash
python test_llm.py
```

**Expected Output:**
```
✅ LLM Response: Yes, I can hear you! How can I help you today?
```

### 📘 Step 5: Prepare Your Data

Place your JSON publication data in the `documents/` folder:

```
documents/
  └── project_1_publications.json
```

**Expected JSON format:**
```json
[
  {
    "id": "1",
    "title": "Publication Title",
    "username": "author_name",
    "publication_description": "Full publication content here..."
  }
]
```

### 📦 Step 6: Build Vector Store

Run the vector store script to process and embed your documents:

```bash
python vector_store.py
```

**Expected Output:**
```
🔍 Loading documents from JSON...
✅ Loaded 45 publications
🧩 Chunking documents...
✅ Created 324 chunks
💾 Adding to vector store...
✅ Vector store ready!
```

### 🎯 Step 7: Run RAG System

```bash
python rag_pipeline.py
```

**Try asking:**
- "What are the main research topics?"
- "Summarize the key findings"
- "What methodologies are discussed?"

Type `quit` to exit.

## 📂 Project Structure

```
my-rag-project/
├── rag_pipeline.py         # Main RAG system
├── vector_store.py          # ChromaDB vector operations
├── json_processor.py        # JSON data loader
├── test_llm.py             # LLM connection test
├── documents/               # Your JSON data
├── chroma_db/              # Auto-generated vector DB
├── .env                     # API keys (create this)
└── rag_env/                # Virtual environment
```

## 🧪 Usage

Run the RAG system:
```bash
python rag_pipeline.py
```

Ask questions about your documents:
- "What are the main research topics?"
- "Summarize the key findings"

Type `quit` to exit.

## 📦 Dependencies

```bash
pip install groq chromadb sentence-transformers tiktoken python-dotenv
```



## 🐛 Troubleshooting

### ❌ "ModuleNotFoundError: No module named 'groq'"
**Solution:**
```bash
# Make sure virtual environment is activated
rag_env\Scripts\activate     # Windows
# source rag_env/bin/activate  # Mac/Linux

# Install packages
pip install groq chromadb sentence-transformers tiktoken python-dotenv
```

### ❌ "GROQ_API_KEY not found"
**Solution:**
1. Check `.env` file exists in project root
2. Verify format: `GROQ_API_KEY=gsk_your_key_here` (no spaces, no quotes)
3. Restart your script after creating `.env`

### ❌ "HTTPError: 401 Unauthorized"
**Solution:**
- Your Groq API key is invalid or expired
- Get a new key: https://console.groq.com/keys
- Update `.env` with new key

### ❌ ChromaDB "Database is locked"
**Solution:**
Delete the `chroma_db/` folder and rebuild:
```bash
rmdir /s chroma_db  # Windows
# rm -rf chroma_db  # Mac/Linux
python vector_store.py
```

### ❌ "No documents loaded"
**Solution:**
1. Check `documents/` folder exists
2. Verify JSON file is named correctly
3. Ensure JSON structure matches format:
```json
[{"id": "1", "title": "...", "username": "...", "publication_description": "..."}]
```

### ❌ Slow embeddings/search
**Solution:**
- First run downloads model (~80MB)
- Subsequent runs are fast

## 🚀 Next Steps

- Add Streamlit web interface
- Support PDF documents
- Add conversation memory
- Deploy as REST API

## 📄 License

MIT License

---

**Questions? Open an issue on GitHub!**
