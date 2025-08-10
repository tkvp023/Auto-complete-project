from search_engine import load_keywords_from_file
from persistence import save_trie
from trie import Trie

trie = Trie()

print("🔄 Loading keywords...")
load_keywords_from_file(trie, "data/keywords.txt")

print("✅ Saving Trie...")
save_trie(trie)

print("✅ Trie saved to trie.pkl")
