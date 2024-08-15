class Solution:
    def countSubstrings(self, s: str) -> str:
        count = 0
        def expand(l, r):
            nonlocal count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        for i in range(len(s)):
            # odd length
            expand(i, i)
            # even length
            expand(i, i + 1)
        return count
