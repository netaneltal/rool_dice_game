import json
from pathlib import Path

# PATH = path = Path(__file__).parent / "game_history.json"
def load_from_json():
    with open("game_history.json","r",encoding="utf-8") as file:
        return json.load(file)
def save_in_json(game):
    list_games = load_from_json()
    list_games.append(game)
    with open("game_history.json", "w", encoding="utf-8") as file:
        json.dump(list_games,file,indent=4)
