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
        for i in range(len(word)):
            w = word[i]
            if not curr.children.get(w):
                return word
            else:
                curr = curr.children.get(w)
                if curr.last:
                    return word[:i+1]
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = Trie()
        for word in dictionary: 
            roots.insert(word)
        out = []
        for word in sentence.split():
            out.append(roots.search(word))
        return ' '.join(out)