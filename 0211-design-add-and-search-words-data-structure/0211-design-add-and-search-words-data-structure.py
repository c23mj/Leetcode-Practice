class WordDictionary:

    def __init__(self):
        self.terminal = False
        self.children = {}

    def addWord(self, word: str) -> None:
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = WordDictionary()
            curr = curr.children[w]
        curr.terminal = True

    def recSearch(self, curr, word: str) -> bool:
        if not word:
            return curr.terminal
        if word[0] == '.':
            for child in curr.children.values():
                if self.recSearch(child, word[1:]):
                    return True
            return False
        if word[0] not in curr.children:
            return False
        return self.recSearch(curr.children[word[0]], word[1:])

    def search(self, word: str) -> bool:
        return self.recSearch(self, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
