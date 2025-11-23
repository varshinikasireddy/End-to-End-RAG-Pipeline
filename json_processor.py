import json
import os
from typing import List, Dict

def load_publications_from_json(json_file_path: str) -> List[Dict]:
    """
    Load publications from the JSON file and structure them for the RAG system
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        documents = []
        
        for publication in data:
            # Extract the main content
            content = publication.get('publication_description', '')
            title = publication.get('title', 'Untitled')
            publication_id = publication.get('id', '')
            username = publication.get('username', '')
            
            # Only include publications with substantial content
            if len(content) > 100:  # At least 100 characters
                documents.append({
                    'id': publication_id,
                    'title': title,
                    'username': username,
                    'content': content,
                    'source': 'json'
                })
        
        print(f"✓ Loaded {len(documents)} publications from JSON")
        return documents
        
    except Exception as e:
        print(f"✗ Error loading JSON file: {str(e)}")
        return []

def print_publication_stats(documents: List[Dict]):
    """Print statistics about the loaded publications"""
    print(f"\n--- Publication Statistics ---")
    print(f"Total publications: {len(documents)}")
    
    # Count characters and words
    total_chars = sum(len(doc['content']) for doc in documents)
    total_words = sum(len(doc['content'].split()) for doc in documents)
    
    print(f"Total characters: {total_chars:,}")
    print(f"Total words: {total_words:,}")
    
    # Show sample of publications
    print(f"\n--- Sample Publications ---")
    for i, doc in enumerate(documents[:3]):  # Show first 3
        print(f"{i+1}. {doc['title']} (by {doc['username']})")
        print(f"   Content preview: {doc['content'][:100]}...")
        print()

# Test the function
if __name__ == "__main__":
    # Make sure the JSON file is in your documents folder
    json_path = "documents/project_1_publications (1).json"
    
    if os.path.exists(json_path):
        publications = load_publications_from_json(json_path)
        print_publication_stats(publications)
    else:
        print(f"JSON file not found at: {json_path}")
        print("Please make sure the JSON file is in the documents/ folder")