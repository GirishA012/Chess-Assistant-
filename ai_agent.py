import os
import faiss
import pickle
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

DATA_DIR = "data"
EMBEDDINGS_FILE = os.path.join(DATA_DIR, "embeddings.pkl")
FAISS_INDEX_FILE = "models/faiss_index"

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index(FAISS_INDEX_FILE)

# Load stored embeddings
with open(EMBEDDINGS_FILE, "rb") as f:
    stored_embeddings = pickle.load(f)

# Load Groq LLM
llm = ChatGroq(model_name="qwen-2.5-32b", api_key=GROQ_API_KEY)

def retrieve_similar_game(current_moves):
    """Finds the closest past game to the current move sequence"""
    query_embedding = model.encode([" ".join(current_moves)]).reshape(1, -1)
    _, idxs = index.search(np.array(query_embedding, dtype=np.float32), k=1)
    return stored_embeddings[idxs[0][0]]

def get_ai_move(current_moves):
    """AI plays the next move based on past games."""
    similar_game = retrieve_similar_game(current_moves)
    prompt = f"""
    You are a chess AI. Given the current moves: {current_moves},
    analyze similar past games: {similar_game},
    and provide ONLY the best next move (e.g., 'e7e5' or 'd2d4'). No explanations.
    """
    
    response = llm.invoke(prompt).content.strip()
    return response

if __name__ == "__main__":
    moves = []  # Start with an empty game history
    
    print("Welcome to Chess Assistant! Play against the AI.")
    while True:
        user_move = input("Your move: ")
        moves.append(user_move)
        ai_move = get_ai_move(moves)
        print(f"AI move: {ai_move}")
        moves.append(ai_move)
