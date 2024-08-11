class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = [False for _ in range(len(s) + 1)]
        memo[0] = True
        for i in range(len(s)):
            idx = i + 1
            for j in range(idx):
                if memo[j] and s[j:idx] in wordSet:
                    memo[idx] = True
                    break
        return memo[-1]
                
        