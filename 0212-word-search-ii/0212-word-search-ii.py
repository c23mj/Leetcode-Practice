class Trie:
    def __init__(self, valid = False):
        self.valid = valid
        self.children = collections.defaultdict(Trie)

    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            curr = curr.children[char]
        curr.valid = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n, wordCount = len(board), len(board[0]), len(words)
        trie = Trie()
        res = []
        for word in words:
            trie.insert(word)
            
        def dfs(r: int, c: int, node: Trie, path: str):
            nonlocal wordCount
            if node.valid:
                res.append(path)
                node.valid = False
                wordCount -= 1
            if wordCount == 0 or r < 0 or r >= m or c < 0 or c >= n:
                return
            char = board[r][c]
            node = node.children.get(char)
            if not node:
                return
            board[r][c] = '#'
            dfs(r + 1, c, node, path + char)
            dfs(r - 1, c, node, path + char)
            dfs(r, c + 1, node, path + char)
            dfs(r, c - 1, node, path + char)
            board[r][c] = char
         
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "")
                if wordCount == 0:
                    return res
        return res

            
            
            
            
        
        
            

        
        
        
        
        