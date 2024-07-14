class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        n = len(t)
        for i in range(len(s)):
            if j < n and s[i] == t[j]:
                j += 1
        return n - j