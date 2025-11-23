# 🤖 RAG System with Groq AI

A smart question-answering system that reads your documents and answers questions using AI. Built with Groq LLM, ChromaDB, and Sentence Transformers.

## ✨ Features

- ⚡ **Lightning Fast**: Get answers in under 1 second
- 🆓 **Free to Use**: Powered by Groq's free tier
- 🔍 **Smart Search**: Finds relevant information from your documents
- 💾 **Local Storage**: Data stored securely on your machine
- 📊 **JSON Support**: Easy document format

## 🚀 Quick Start

### 1. Get Your Free Groq API Key

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up and create an API key
3. Copy the key (starts with `gsk_...`)

### 2. Install

```bash
# Clone this repository
git clone <your-repo-url>
cd my-rag-project

# Create virtual environment
python -m venv rag_env

# Activate it
rag_env\Scripts\activate  # Windows
# source rag_env/bin/activate  # Mac/Linux

# Install dependencies
pip install groq chromadb sentence-transformers tiktoken python-dotenv
```

### 3. Configure

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### 4. Add Your Documents

Place JSON files in the `documents/` folder:

```json
[
  {
    "id": "1",
    "title": "Document Title",
    "username": "author",
    "publication_description": "Your document content..."
  }
]
```

### 5. Run

```bash
# Test connection
python test_llm.py

# Run the RAG system
python rag_pipeline.py
```

Ask questions about your documents and get AI-powered answers!

## 📁 Project Structure

```
my-rag-project/
├── rag_pipeline.py          # Main RAG system
├── vector_store.py          # Document storage & search
├── json_processor.py        # Document loader
├── test_llm.py             # Connection test
├── .env                     # API key (create this)
├── documents/               # Your JSON files
└── chroma_db/              # Auto-generated database
```

## 🛠 How It Works

1. **Load**: Reads documents from JSON files
2. **Chunk**: Breaks documents into searchable pieces
3. **Embed**: Converts text to vectors using AI
4. **Store**: Saves in ChromaDB for fast search
5. **Search**: Finds relevant content for your question
6. **Answer**: Groq AI generates the answer

## 💡 Usage Example

```python
from rag_pipeline import GroqRAGSystem

# Initialize
rag = GroqRAGSystem()

# Ask questions
response, sources = rag.query("What are the main topics?")
print(response)
```

## 🐛 Troubleshooting

**"ModuleNotFoundError: No module named 'groq'"**
```bash
pip install groq chromadb sentence-transformers tiktoken python-dotenv
```

**"GROQ_API_KEY not found"**
- Check `.env` file exists
- Verify the key format: `GROQ_API_KEY=gsk_...`

**ChromaDB locked**
```bash
# Delete and rebuild
rmdir /s chroma_db  # Windows
# rm -rf chroma_db  # Mac/Linux
python rag_pipeline.py
```

## ⚙️ Configuration

Edit `vector_store.py` for chunking:
```python
chunk_size = 512    # Tokens per chunk
overlap = 50        # Overlap between chunks
```

Edit `rag_pipeline.py` for search:
```python
n_results = 3       # Number of documents to retrieve
self.model = "llama-3.1-8b-instant"  # Groq model
```

## 📦 Dependencies

- `groq` - AI model API
- `chromadb` - Vector database
- `sentence-transformers` - Text embeddings
- `tiktoken` - Token counting
- `python-dotenv` - Environment variables

## 🌟 Why This Stack?

- **Groq**: Ultra-fast AI inference (free tier available)
- **ChromaDB**: Efficient local vector storage
- **Sentence Transformers**: High-quality embeddings

## 🚀 Next Steps

- Add web interface with Streamlit
- Support PDF documents
- Add conversation memory
- Deploy as REST API

## 📄 License

MIT License - free to use for learning and projects

## 🤝 Contributing

Contributions welcome! Open an issue or submit a PR.

---

**Built with ❤️ using Groq AI**
