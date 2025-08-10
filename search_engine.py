from trie import Trie
from rapidfuzz import process

trie = Trie()

def load_keywords_from_file(trie_obj, file_path="data/keywords.txt"):
    with open(file_path, "r") as f:
        for line in f:
            word = line.strip()
            if word:
                trie_obj.insert(word)

def get_all_words(node, prefix='', words=None):
    if words is None:
        words = []
    if node.is_end:
        words.append(prefix)
    for ch in node.children:
        get_all_words(node.children[ch], prefix + ch, words)
    return words

def fuzzy_suggest(trie_obj, prefix, limit=5):
    all_words = get_all_words(trie_obj.root)
    results = process.extract(prefix, all_words, limit=limit)
    return [match[0] for match in results]
