class Trie:

    def __init__(self):
        self.last = False
        self.children = dict()

    def insert(self, word: str) -> None:
        curr = self
        for w in word:
            if not curr.children.get(w):
                child = Trie()
                curr.children[w] = child
                curr = child
            else:
                curr = curr.children[w]
        curr.last = True

    def search(self, word: str) -> bool:
        curr = self
        for w in word:
            if not curr.children.get(w):
                return False
            else:
                curr = curr.children.get(w)
        return curr.last

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for p in prefix:
            if not curr.children.get(p):
                return False
            else:
                curr = curr.children[p]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)