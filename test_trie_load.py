from persistence import load_trie

trie = load_trie()
results = trie.suggest("m")

print("Suggestions for 'm':", results)
