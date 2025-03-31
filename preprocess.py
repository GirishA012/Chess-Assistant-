import chess.pgn
import os
import pickle
from sentence_transformers import SentenceTransformer

DATA_DIR = "data"
PGN_FILE = os.path.join(DATA_DIR, "games.pgn")
EMBEDDINGS_FILE = os.path.join(DATA_DIR, "embeddings.pkl")

model = SentenceTransformer("all-MiniLM-L6-v2")  # Small and efficient model

def extract_moves_from_pgn():
    moves_list = []
    with open(PGN_FILE) as pgn_file:
        while True:
            game = chess.pgn.read_game(pgn_file)
            if game is None:
                break
            board = game.board()
            moves = [move.uci() for move in game.mainline_moves()]
            moves_list.append(" ".join(moves))
    return moves_list

def create_embeddings():
    moves_list = extract_moves_from_pgn()
    embeddings = model.encode(moves_list)

    with open(EMBEDDINGS_FILE, "wb") as f:
        pickle.dump(embeddings, f)

    print(f"✅ Embeddings saved at {EMBEDDINGS_FILE}")

if __name__ == "__main__":
    create_embeddings()
