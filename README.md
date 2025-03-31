# Chess Assistant ♟️

## Project Overview
**Chess Assistant** is an AI-powered chess bot that allows users to play against a model trained on their own **Chess.com match history**. The system retrieves past game data, processes it into vector embeddings using **FAISS**, and implements a **RAG (Retrieval-Augmented Generation) pipeline**. The core AI engine is powered by **Groq’s Qwen LLM**, enabling strategic chess play based on the user's historical performance.

---

## Features
- ✅ **Fetch Chess.com Match History** – Retrieves PGN files of past games via the Chess.com API.
- ✅ **Game Embedding Storage** – Converts PGN files into vector embeddings using **FAISS**.
- ✅ **RAG Pipeline for AI Understanding** – Enables intelligent game insights and move predictions.
- ✅ **Groq Qwen LLM as Chess Bot** – Plays against users, analyzing past strategies and improving gameplay.
- ✅ **Interactive Play** – Allows users to challenge their own AI bot, which learns from their history.

---

## Tech Stack
- 🔹 **Python** – Core programming language
- 🔹 **Chess.com API** – Fetching user match history
- 🔹 **FAISS** – Vector storage for efficient retrieval
- 🔹 **Groq Qwen LLM** – AI model for move predictions
- 🔹 **LangChain** – For RAG pipeline and model interaction

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/chess-assistant.git
cd chess-assistant
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file and add the following:
```env
CHESS_COM_API_KEY=your_api_key_here
GROQ_LLM_API_KEY=your_api_key_here
```

### 5. Run the Project
```bash
python ai_agent.py
```

---

## File Structure
```
Chess Assistant
├── data                 # Stores raw PGN and processed data
├── models               # Stores trained models and embeddings
├── venv                 # Virtual environment (excluded in .gitignore)
├── .env                 # API keys (excluded in .gitignore)
├── ai_agent.py          # Runs the AI chess bot
├── fetch_games.py       # Fetches Chess.com match history
├── preprocess.py        # Converts PGN files into embeddings
├── rag_pipeline.py      # RAG pipeline for intelligent retrieval
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
```

---

## Usage
1. **Run `fetch_games.py`** to retrieve past match data from Chess.com.
2. **Run `preprocess.py`** to convert PGN files into embeddings using FAISS.
3. **Run `rag_pipeline.py`** to create the AI knowledge base.
4. **Run `ai_agent.py`** to start playing against your personalized AI chess bot.

---

## Future Enhancements 🚀
- [ ] **Web UI for Chess AI** using Streamlit
- [ ] **Improve AI Move Prediction** by fine-tuning strategies
- [ ] **Add Voice Commands** to make moves via speech

---

