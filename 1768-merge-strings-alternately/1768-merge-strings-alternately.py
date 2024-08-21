class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        out = []
        for i in range(n):
            out.append(word1[i])
            out.append(word2[i])
        for i in range(n, len(word1)):
            out.append(word1[i])
        for i in range(n, len(word2)):
            out.append(word2[i])
        return ''.join(out)
        
            