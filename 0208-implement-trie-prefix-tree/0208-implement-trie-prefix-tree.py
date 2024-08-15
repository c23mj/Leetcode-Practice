class Trie:
    def __init__(self, valid = False):
        self.valid = valid
        self.children = collections.defaultdict(Trie)

    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            curr = curr.children[char]
        curr.valid = True

    def search(self, word: str) -> bool:
        curr = self
        for char in word:
            if not curr.children.get(char):
                return False
            curr = curr.children[char]
        return curr.valid
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            if not curr.children.get(char):                
                return False
            curr = curr.children[char]
        return True