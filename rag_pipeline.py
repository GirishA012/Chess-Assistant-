import faiss
import numpy as np
import pickle
import os

DATA_DIR = "data"
EMBEDDINGS_FILE = os.path.join(DATA_DIR, "embeddings.pkl")
FAISS_INDEX_FILE = "models/faiss_index"

def build_faiss_index():
    with open(EMBEDDINGS_FILE, "rb") as f:
        embeddings = pickle.load(f)

    d = embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(np.array(embeddings, dtype=np.float32))

    faiss.write_index(index, FAISS_INDEX_FILE)
    print(f"✅ FAISS index saved to {FAISS_INDEX_FILE}")

if __name__ == "__main__":
    os.makedirs("models", exist_ok=True)
    build_faiss_index()
