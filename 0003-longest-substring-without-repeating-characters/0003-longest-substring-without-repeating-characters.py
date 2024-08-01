class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxString = 0
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxString = max(maxString, r - l + 1)
        return maxString