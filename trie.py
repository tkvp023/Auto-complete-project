class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.freq = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        node.freq += 1

    def suggest(self, prefix, k=5):
        def dfs(node, path, suggestions):
            if node.is_end:
                suggestions.append((-node.freq, ''.join(path)))
            for ch in node.children:
                dfs(node.children[ch], path + [ch], suggestions)

        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        suggestions = []
        dfs(node, list(prefix), suggestions)
        suggestions.sort()
        return [word for _, word in suggestions[:k]]
