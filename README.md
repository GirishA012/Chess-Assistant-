# Chess Assistant ♟️

## Project Overview
**Chess Assistant** is an **AI-powered** chess bot that allows users to play against a model trained on their anyone's **Chess.com match history**. The system retrieves past game data, processes it into vector embeddings using **FAISS**, and implements a **RAG (Retrieval-Augmented Generation) pipeline**. The core AI engine is powered by **Groq’s Qwen LLM**, enabling strategic chess play based on the user's historical performance.

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

