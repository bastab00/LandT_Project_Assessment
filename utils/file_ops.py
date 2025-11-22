import json
import os

DATA_FILE = "data/quiz_data.json"
ID_START = 101

def load_data():
    base = {"next_id": ID_START, "students": {}}

    if not os.path.exists(DATA_FILE):
        return base
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "next_id" not in data or "students" not in data:
            return base
        return data

    except:
        return base


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
