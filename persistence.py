import json, pickle
from trie import Trie

def save_to_json(word_freq, file_path="data/keywords.json"):
    with open(file_path, "w") as f:
        json.dump(word_freq, f)

def load_from_json(file_path="data/keywords.json"):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except:
        return {}

def save_trie(trie_obj, file_path="trie.pkl"):
    with open(file_path, "wb") as f:
        pickle.dump(trie_obj, f)

def load_trie(file_path="trie.pkl"):
    try:
        with open(file_path, "rb") as f:
            return pickle.load(f)
    except:
        return Trie()
