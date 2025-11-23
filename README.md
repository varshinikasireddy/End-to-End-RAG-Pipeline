# RAG System with Groq, ChromaDB & Sentence Transformers

A Retrieval-Augmented Generation (RAG) system that enables semantic search and question-answering over JSON publication data using Groq LLM, ChromaDB vector database, and Sentence Transformers.

## Features

- **Fast LLM Inference**: Powered by Groq's ultra-fast API
- **Semantic Search**: ChromaDB vector database for intelligent document retrieval
- **Local Embeddings**: Sentence Transformers for cost-effective embeddings
- **JSON Data Processing**: Automatically processes and indexes publication data
- **Persistent Storage**: ChromaDB saves embeddings locally for reuse
- **Context-Aware Responses**: Retrieves relevant documents before generating answers

## System Architecture

- **Data Layer**: JSON publication storage
- **Processing Layer**: Token-based chunking with overlap
- **Vector Layer**: ChromaDB with sentence embeddings
- **LLM Layer**: Groq API for response generation

## How It Works

1. **Document Processing**: JSON publications are loaded and chunked into manageable pieces
2. **Embedding Creation**: Each chunk is converted to vector embeddings using Sentence Transformers
3. **Vector Storage**: Embeddings are stored in ChromaDB for efficient similarity search
4. **Query Processing**: User queries are embedded and matched against stored vectors
5. **Context Retrieval**: Top relevant chunks are retrieved based on similarity
6. **Response Generation**: Retrieved context is sent to Groq LLM for answer generation

## Prerequisites

- Python 3.8+
- Groq API Key (get for free at [console.groq.com](https://console.groq.com/))

## Installation

1. Clone this repository
2. Create a virtual environment:
```bash
python -m venv rag_env
```

3. Activate the virtual environment:
```bash
# Windows
rag_env\Scripts\activate

# Mac/Linux
source rag_env/bin/activate
```

4. Install dependencies:
```bash
pip install groq chromadb sentence-transformers tiktoken python-dotenv
```

5. Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_api_key_here
```

## Project Structure

```
my-rag-project/
├── rag_pipeline.py          # Main RAG system implementation
├── vector_store.py           # ChromaDB vector store management
├── json_processor.py         # JSON data loading and processing
├── test_llm.py              # LLM testing utilities
├── .env                      # Environment variables (not in git)
├── .gitignore               # Git ignore rules
├── documents/               # Your JSON data files
│   └── project_1_publications.json
└── chroma_db/              # Vector database (auto-generated)
```

## Usage

### Prepare Your Data

Place your JSON publication data in the `documents/` folder:
```
documents/
  └── project_1_publications.json
```

Expected JSON format:
```json
[
  {
    "id": "1",
    "title": "Publication Title",
    "username": "author_name",
    "publication_description": "Full publication content..."
  }
]
```

### Run the System

```bash
python rag_pipeline.py
```

## Key Components

### 1. **Vector Store** (`vector_store.py`)
- Uses ChromaDB for persistent vector storage
- `all-MiniLM-L6-v2` for embeddings
- Smart text chunking with overlap
- Semantic search capabilities

### 2. **JSON Processor** (`json_processor.py`)
- Loads publication data from JSON
- Filters publications (min 100 characters)
- Structures data for RAG system

### 3. **RAG Pipeline** (`rag_pipeline.py`)
- Integrates vector search + LLM
- Uses Groq's `llama-3.1-8b-instant` model
- Context-aware prompt engineering
- Returns answers with source documents

## Configuration

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

## Dependencies

```
groq                    # Groq LLM API
chromadb               # Vector database
sentence-transformers  # Embedding models
tiktoken              # Token counting
python-dotenv         # Environment variables
```

## Troubleshooting

### "Groq package not installed"
```bash
pip install groq
```

### "GROQ_API_KEY not found"
- Check your `.env` file exists
- Verify the API key is correct
- Ensure `.env` is in the project root

### ChromaDB Issues
Delete the `chroma_db/` folder and re-run:
```bash
rmdir /s chroma_db  # Windows
# rm -rf chroma_db  # Mac/Linux
python rag_pipeline.py
```

## Performance

- **Search Speed**: ~50ms (ChromaDB)
- **LLM Response**: ~100-500ms (Groq)
- **Total Query Time**: < 1 second

## License

MIT License - feel free to use this project for learning and development.

## Acknowledgments

- [Groq](https://groq.com/) for ultra-fast LLM inference
- [ChromaDB](https://www.trychroma.com/) for vector storage
- [Sentence Transformers](https://www.sbert.net/) for embeddings
