import requests
import os

USERNAME = "Grigg12"  # Your Chess.com username
DATA_DIR = "data"
PGN_FILE = os.path.join(DATA_DIR, "games.pgn")

# ✅ Add a User-Agent header to bypass Chess.com's bot protection
HEADERS = {
    "User-Agent": "ChessAssistantBot/1.0 (contact: your-email@example.com)"
}

os.makedirs(DATA_DIR, exist_ok=True)

def fetch_chess_games():
    url = f"https://api.chess.com/pub/player/{USERNAME}/games/archives"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 403:
        print("❌ Error 403: Access Forbidden. Make sure your Chess.com games are public.")
        print("🔹 Go to Chess.com > Settings > Privacy > Enable Public Game Archive.")
        return
    elif response.status_code != 200:
        print(f"❌ Error: Chess.com API returned status code {response.status_code}")
        return
    
    try:
        archives = response.json().get("archives", [])
    except requests.exceptions.JSONDecodeError:
        print("❌ Error: Failed to decode JSON. Possible empty response or Chess.com API issue.")
        return

    if not archives:
        print("⚠️ No archives found. Make sure your games are public.")
        return

    with open(PGN_FILE, "w") as pgn_file:
        for archive_url in archives:
            games_response = requests.get(f"{archive_url}/pgn", headers=HEADERS)

            if games_response.status_code != 200 or not games_response.text.strip():
                print(f"⚠️ Skipping empty or invalid PGN data from {archive_url}")
                continue

            pgn_file.write(games_response.text + "\n\n")
    
    print(f"✅ All games saved to {PGN_FILE}")

if __name__ == "__main__":
    fetch_chess_games()
