class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        memo = [0 for i in range(26)]
        for char in s:
            currIdx = ord(char) - ord('a')
            best_pre = max(memo[max(currIdx - k, 0):min(currIdx + k + 1, 26)])
            memo[currIdx] = max(best_pre + 1, memo[currIdx])
        return max(memo)
