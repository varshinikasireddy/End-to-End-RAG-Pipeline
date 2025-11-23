import chromadb
from sentence_transformers import SentenceTransformer
import tiktoken
from typing import List, Dict
import json
import os

class VectorStore:
    def __init__(self, persist_directory: str = "chroma_db"):
        self.persist_directory = persist_directory
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(name="publications")
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.encoder = tiktoken.get_encoding("cl100k_base")
        
    def count_tokens(self, text: str) -> int:
        """Count tokens in text for chunking"""
        return len(self.encoder.encode(text))
    
    def chunk_text(self, text: str, chunk_size: int = 512, overlap: int = 50) -> List[str]:
        """Split text into overlapping chunks"""
        tokens = self.encoder.encode(text)
        chunks = []
        
        for i in range(0, len(tokens), chunk_size - overlap):
            chunk_tokens = tokens[i:i + chunk_size]
            chunk_text = self.encoder.decode(chunk_tokens)
            chunks.append(chunk_text)
            
            if i + chunk_size >= len(tokens):
                break
                
        return chunks
    
    def add_documents(self, documents: List[Dict]):
        """Add documents to the vector store with chunking"""
        all_chunks = []
        all_metadatas = []
        all_ids = []
        
        for doc in documents:
            # Split content into chunks
            chunks = self.chunk_text(doc['content'])
            
            for i, chunk in enumerate(chunks):
                all_chunks.append(chunk)
                all_metadatas.append({
                    'publication_id': doc['id'],
                    'title': doc['title'],
                    'username': doc['username'],
                    'source': doc['source'],
                    'chunk_index': i,
                    'total_chunks': len(chunks)
                })
                all_ids.append(f"{doc['id']}_{i}")
        
        # Generate embeddings and add to collection
        if all_chunks:
            embeddings = self.embedding_model.encode(all_chunks).tolist()
            self.collection.add(
                embeddings=embeddings,
                documents=all_chunks,
                metadatas=all_metadatas,
                ids=all_ids
            )
            
        print(f"✓ Added {len(all_chunks)} chunks from {len(documents)} publications")
        return len(all_chunks)
    
    def search(self, query: str, n_results: int = 5) -> List[Dict]:
        """Search for similar documents"""
        query_embedding = self.embedding_model.encode([query]).tolist()
        
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=n_results,
            include=['documents', 'metadatas', 'distances']
        )
        
        formatted_results = []
        for i in range(len(results['documents'][0])):
            formatted_results.append({
                'content': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'distance': results['distances'][0][i]
            })
        
        return formatted_results

# Test the vector store
if __name__ == "__main__":
    from json_processor import load_publications_from_json
    
    # Load publications
    publications = load_publications_from_json("documents/project_1_publications (1).json")
    
    # Initialize vector store
    print("Initializing vector store...")
    vector_store = VectorStore()
    
    # Add documents
    print("Adding documents to vector store...")
    chunk_count = vector_store.add_documents(publications)
    
    # Test search
    print("\nTesting search functionality...")
    test_queries = [
        "RAG memory",
        "computer vision models", 
        "time series forecasting"
    ]
    
    for query in test_queries:
        print(f"\nSearching for: '{query}'")
        results = vector_store.search(query, n_results=2)
        for i, result in enumerate(results):
            print(f"  {i+1}. {result['metadata']['title']} (distance: {result['distance']:.3f})")