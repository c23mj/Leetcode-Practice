class Trie:

    def __init__(self, valid = False):
        self.valid = False
        self.children = dict()

    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.valid = True

    def search(self, word: str) -> bool:
        curr = self
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.valid
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)