class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen, sLen = 0, len(s)
        def expand(l, r):
            nonlocal resLen, sLen, res
            while l >= 0 and r < sLen and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1

        for i in range(sLen):
            # odd length
            expand(i, i)
            # even length
            expand(i, i + 1)
        return res
