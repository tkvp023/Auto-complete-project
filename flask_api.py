from flask import Flask, request, jsonify
from persistence import load_trie, save_trie

app = Flask(__name__)
trie = load_trie()

from search_engine import fuzzy_suggest

@app.route("/autocomplete")
def autocomplete():
    prefix = request.args.get("prefix", "")
    suggestions = fuzzy_suggest(trie, prefix)
    return jsonify(suggestions)


@app.route("/add", methods=["POST"])
def add_word():
    data = request.json
    word = data.get("word")
    if word:
        trie.insert(word)
        save_trie(trie)
        return jsonify({"message": "Word added"}), 201
    return jsonify({"error": "Word not provided"}), 400

if __name__ == "__main__":
    app.run(debug=True)
