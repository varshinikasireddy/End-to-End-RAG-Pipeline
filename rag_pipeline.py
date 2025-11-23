import os
from dotenv import load_dotenv
try:
    from groq import Groq
except ImportError:
    print("❌ Groq package not installed. Run: pip install groq")
    exit(1)

from vector_store import VectorStore
from json_processor import load_publications_from_json
import textwrap

load_dotenv()

class GroqRAGSystem:
    def __init__(self):
        # Check if Groq API key is set
        if not os.getenv('GROQ_API_KEY'):
            print("❌ GROQ_API_KEY not found in .env file")
            print("Please get a FREE API key from: https://console.groq.com/")
            print("And add it to your .env file")
            exit(1)
            
        self.vector_store = VectorStore()
        self.client = Groq(api_key=os.getenv('GROQ_API_KEY'))
        self.model = "llama-3.1-8b-instant"  # Free, fast model
        
    def query(self, question: str, n_results: int = 3):
        """Query the RAG system with a question"""
        
        # 1. Search for relevant documents
        print("🔍 Searching for relevant documents...")
        search_results = self.vector_store.search(question, n_results=n_results)
        
        # 2. Format context from search results
        context = self._format_context(search_results)
        
        # 3. Create enhanced prompt with context
        prompt = self._create_prompt(question, context)
        
        # 4. Get response from Groq (super fast!)
        print("⚡ Generating answer with Groq...")
        response = self._get_groq_response(prompt)
        
        return response, search_results
    
    def _format_context(self, search_results: list) -> str:
        """Format search results into context string"""
        context_parts = []
        
        for i, result in enumerate(search_results):
            title = result['metadata']['title']
            username = result['metadata']['username']
            content = result['content']
            distance = result['distance']
            
            context_parts.append(
                f"Document {i+1} (Relevance: {1-distance:.3f}):\n"
                f"Title: {title}\n"
                f"Author: {username}\n"
                f"Content: {content}\n"
                f"{'-'*50}"
            )
        
        return "\n".join(context_parts)
    
    def _create_prompt(self, question: str, context: str) -> str:
        """Create the RAG prompt with context"""
        
        prompt = f"""You are an AI assistant with access to technical publications about machine learning, AI, and data science.

Based on the following context from relevant publications, please answer the user's question. If the context doesn't contain enough information to fully answer the question, you can use your general knowledge but please indicate what information comes from the provided context vs. your general knowledge.

CONTEXT:
{context}

QUESTION: {question}

Please provide a comprehensive answer that:
1. Directly addresses the question
2. Cites specific information from the provided context when possible
3. Is well-structured and easy to understand
4. If using information from specific documents, mention which ones

ANSWER:"""
        
        return prompt
    
    def _get_groq_response(self, prompt: str) -> str:
        """Get response from Groq (much faster than OpenAI!)"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant that provides accurate, technical information about machine learning and AI."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=1000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error generating response: {str(e)}"

def main():
    """Main function to run the Groq RAG system"""
    print("🚀 Initializing Groq RAG System...")
    print("💡 Using FREE Groq API with Llama 3 (super fast!)")
    
    try:
        rag = GroqRAGSystem()
    except Exception as e:
        print(f"❌ Failed to initialize RAG system: {e}")
        return
    
    print("✅ Groq RAG System Ready! Ask questions about the publications.")
    print("Type 'quit' to exit.\n")
    
    # Test questions to try
    print("💡 Try these questions:")
    print("  - How can I add memory to RAG applications?")
    print("  - What are auto-encoders used for?") 
    print("  - Tell me about time series forecasting\n")
    
    while True:
        question = input("🤔 Your question: ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
            
        if not question:
            continue
            
        print("\n" + "="*60)
        
        try:
            answer, search_results = rag.query(question)
            
            print(f"\n📚 Sources used ({len(search_results)} documents):")
            for i, result in enumerate(search_results):
                relevance_score = 1 - result['distance']
                print(f"   {i+1}. {result['metadata']['title']}")
                print(f"      by {result['metadata']['username']} (relevance: {relevance_score:.3f})")
            
            print(f"\n💡 Answer:")
            print(textwrap.fill(answer, width=80))
            print("\n" + "="*60 + "\n")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            print("Please try again with a different question.\n")

if __name__ == "__main__":
    main()