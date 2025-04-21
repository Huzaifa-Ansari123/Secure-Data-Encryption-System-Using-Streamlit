import json
import os

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

stored_data = load_data()

def add_entry(key, encrypted_text, hashed_passkey):
    stored_data[key] = {
        "encrypted_text": encrypted_text,
        "passkey": hashed_passkey
    }
    save_data(stored_data)

def get_entry(key):
    return stored_data.get(key)
