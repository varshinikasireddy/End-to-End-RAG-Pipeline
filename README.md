# 🚀 RAG System with Groq, ChromaDB & Sentence Transformers

**A complete beginner-friendly guide with step-by-step instructions**

This project demonstrates how to build a **Retrieval-Augmented Generation (RAG) System** using:

- ⚡ **Groq LLMs** (super-fast inference)
- 🗄️ **ChromaDB** (local vector database)
- 🧠 **Sentence Transformers** (embeddings)
- 📊 **JSON Data Processing** (publication documents)
- 🐍 **Python**

This README will help you understand, set up, run, and extend your RAG system — **even if you are new to AI/LLMs**.

---

## 🧠 What You Will Build

By the end of this project, you will have:

✅ A working LLM connection using **Groq**  
✅ A document loader for your **JSON publications**  
✅ A vector database (**ChromaDB**)  
✅ A text chunking & embeddings pipeline  
✅ A **RAG pipeline** that answers questions with citations  
✅ Fully working code files:
- `test_llm.py`
- `json_processor.py`
- `vector_store.py`
- `rag_pipeline.py`

---

## 🌟 Key Features

- 🚀 **Lightning Fast**: Powered by Groq's ultra-fast LLM inference
- 🔍 **Semantic Search**: ChromaDB vector database for intelligent document retrieval
- 📊 **JSON Data Processing**: Automatically processes publication data
- 🧠 **Intelligent Chunking**: Smart text chunking with overlap for better context
- 💾 **Persistent Storage**: ChromaDB saves embeddings locally
- 🎯 **Context-Aware Answers**: Retrieves most relevant documents before generating responses
- 💰 **Cost-Effective**: Local embeddings (no API costs)
- 🔧 **Modular Design**: Clean, reusable code structure

---

## 🏗️ System Architecture

```
User Question
     ↓
[Vector Search] → ChromaDB (finds relevant docs)
     ↓
[Context Building] → Combines relevant publications
     ↓
[LLM Generation] → Groq API (llama-3.1-8b-instant)
     ↓
Generated Answer
```

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
├── 📄 rag_pipeline.py         # Main RAG system
├── 📄 vector_store.py          # ChromaDB vector operations
├── 📄 json_processor.py        # JSON data loader
├── 📄 test_llm.py             # LLM connection test
├── 📁 documents/               # Your JSON data
│   └── project_1_publications.json
├── 📁 chroma_db/              # Auto-generated vector DB
├── 🔐 .env                     # API keys (create this)
└── 📁 rag_env/                # Virtual environment
```

### 🔍 Component Details

#### `json_processor.py`
Loads publication data from JSON files:
```python
def load_publications(file_path):
    # Reads JSON
    # Filters publications (min 100 chars)
    # Returns structured documents
```

**What it does:**
- Reads JSON file from `documents/` folder
- Extracts: `id`, `title`, `username`, `publication_description`
- Filters short publications (< 100 characters)
- Returns clean list of documents

#### `vector_store.py`
Manages ChromaDB vector operations:
```python
class VectorStore:
    # Creates embeddings with SentenceTransformer
    # Chunks text (512 tokens, 50 overlap)
    # Stores in ChromaDB
    # Searches by similarity
```

**What it does:**
- **Chunking**: Splits long texts into 512-token chunks with 50-token overlap
- **Embedding**: Converts text to vectors using `all-MiniLM-L6-v2`
- **Storage**: Saves vectors to persistent ChromaDB (`chroma_db/` folder)
- **Search**: Finds most similar chunks to your query

#### `rag_pipeline.py`
Main RAG system:
```python
class GroqRAGSystem:
    def query(self, question):
        # 1. Search vector store for relevant chunks
        # 2. Format context from top results
        # 3. Call Groq LLM with context
        # 4. Return answer + source documents
```

**What it does:**
- Takes your question
- Searches vector store for relevant information
- Sends context + question to Groq LLM
- Returns AI-generated answer with sources

## 🛠 System Architecture

```
📝 User Query
    ↓
🔍 Vector Search (find similar documents)
    ↓
📖 Context Retrieval (get top 3 chunks)
    ↓
🤖 Groq LLM (generate answer)
    ↓
✅ Response + Sources
```

**Detailed Flow:**

1. **📥 Data Ingestion**: JSON publications loaded and filtered
2. **🧩 Chunking**: Split into 512-token chunks with 50-token overlap
3. **🔢 Embedding**: Each chunk converted to vector using `all-MiniLM-L6-v2`
4. **💾 Storage**: Vectors stored in persistent ChromaDB
5. **🔍 Query**: User question embedded and matched against vectors
6. **📖 Retrieval**: Top 3 relevant chunks retrieved by similarity
7. **🤖 Generation**: Groq LLM generates answer using retrieved context

## 💡 Usage Examples

### Basic Query
```python
from rag_pipeline import GroqRAGSystem

# Initialize the system
rag = GroqRAGSystem()

# Load your data
from json_processor import load_publications_from_json
docs = load_publications_from_json("documents/project_1_publications.json")
rag.vector_store.add_documents(docs)

# Ask questions
response, sources = rag.query("What are the main topics in the publications?")
print(response)
```

### Interactive Mode
```python
# Run the main script
python rag_pipeline.py

# Then ask questions interactively:
# >>> What is discussed about AI?
# >>> Summarize the key findings
# >>> (type 'quit' to exit)
```

## 🧪 Testing Your Setup

### Test 1: LLM Connection
```bash
python test_llm.py
```
✅ **Pass**: You see a response from the LLM

### Test 2: Vector Store
```bash
python vector_store.py
```
✅ **Pass**: See "✅ Vector store ready!" message

### Test 3: Full RAG System
```bash
python rag_pipeline.py
```
Try: "What are the main topics?"
✅ **Pass**: Get a relevant answer with sources

## 📦 Dependencies

```txt
groq                    # Groq LLM API
chromadb               # Vector database
sentence-transformers  # Embedding models
tiktoken              # Token counting
python-dotenv         # Environment variables
```

## 🔑 Why These Technologies?

### 🚀 Groq
- ⚡ **Fast**: Up to 18x faster than standard inference
- 🆓 **Free**: Generous free tier for development
- 🎯 **Quality**: Access to Llama, Mixtral models
- 🔧 **Simple**: OpenAI-compatible API

### 💾 ChromaDB
- 🏠 **Local**: Runs on your machine (no cloud needed)
- 💪 **Persistent**: Data saved between runs
- ⚡ **Fast**: Optimized similarity search
- 🐍 **Pythonic**: Easy to use API

### 🎯 Sentence Transformers
- 🎓 **Proven**: State-of-the-art embeddings
- 📦 **Lightweight**: `all-MiniLM-L6-v2` is only 80MB
- ⚡ **Fast**: Quick embedding generation
- 🔓 **Open**: Free and open source

## ⚙️ Configuration

### Chunking Parameters
Edit `vector_store.py`:
```python
chunk_size = 512    # Tokens per chunk
overlap = 50        # Token overlap between chunks
```

### Search Results
Edit `rag_pipeline.py`:
```python
n_results = 3       # Number of documents to retrieve
```

### LLM Model
Edit `rag_pipeline.py`:
```python
self.model = "llama-3.1-8b-instant"  # Fast and free
# Or try: "mixtral-8x7b-32768" for longer context
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
- First run is slower (downloads model ~80MB)
- Subsequent runs are fast
- Check your internet connection for first-time setup

## 🎨 Customization

### Change Embedding Model
Edit `vector_store.py`:
```python
self.embedding_model = SentenceTransformer('all-mpnet-base-v2')  # Better quality
# Or: 'paraphrase-multilingual-MiniLM-L12-v2'  # Multilingual support
```

### Change LLM Model
Edit `rag_pipeline.py`:
```python
self.model = "mixtral-8x7b-32768"  # Longer context window
# Or: "llama-3.1-70b-versatile"  # More powerful
```

### Adjust Chunk Size
Edit `vector_store.py`:
```python
chunk_size = 1024   # Larger chunks (more context)
overlap = 100       # More overlap (better continuity)
```

### Change Number of Results
Edit `rag_pipeline.py`:
```python
results = self.vector_store.search(query, n_results=5)  # Get top 5
```

## 📊 Performance Metrics

| Component | Speed | Notes |
|-----------|-------|-------|
| Document Loading | < 1s | For ~50 publications |
| Embedding Generation | ~2-5s | First time (downloads model) |
| Vector Search | ~50ms | Per query |
| LLM Response | ~100-500ms | Depends on answer length |
| **Total Query Time** | **< 1 second** | After initial setup |

## 🚀 Next Improvements

Here are some ways to enhance this project:

### 1. 🌐 **Add Web Interface**
```bash
pip install streamlit
```
Create `app.py` with Streamlit UI for easy interaction

### 2. 🔄 **Hybrid Search**
Combine vector search with keyword search (BM25) for better results

### 3. 📊 **Add Conversation Memory**
Store chat history to enable follow-up questions

### 4. 🎯 **Multi-document Support**
Extend to handle PDFs, web pages, or other document types

### 5. ⚡ **Caching**
Cache frequent queries to improve response time

### 6. 📈 **Analytics Dashboard**
Track most asked questions, response quality, etc.

### 7. 🔐 **User Authentication**
Add user management for multi-user scenarios

### 8. 🌍 **Multi-language Support**
Use multilingual embedding models

### 9. 🎛 **Advanced Filters**
Filter by author, date, topic, etc.

### 10. 📱 **API Endpoint**
Create REST API with FastAPI for integration

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - feel free to use this project for learning and development.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for ultra-fast LLM inference
- [ChromaDB](https://www.trychroma.com/) for vector storage
- [Sentence Transformers](https://www.sbert.net/) for embeddings

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Happy Building! 🎉**
