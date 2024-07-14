class Solution:
    def longestPalindrome(self, s: str) -> int:
        letterCounts = defaultdict(int)
        for char in s:
            letterCounts[char] += 1
        totalEven = sum([val//2 * 2 for val in letterCounts.values()])
        return totalEven if totalEven == len(s) else totalEven + 1