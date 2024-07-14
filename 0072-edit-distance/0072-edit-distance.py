class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # naive recursive solution
        # if len(word1) == 0: return len(word2)
        # if len(word2) == 0: return len(word1)
        # if word1[0] == word2[0]: return self.minDistance(word1[1:], word2[1:])
        # return 1 + min(
        #     self.minDistance(word1, word2[1:]),
        #     self.minDistance(word1[1:], word2[1:]),
        #     self.minDistance(word1[1:], word2)
        # )
        n, m = len(word1), len(word2)
        if n == 0: return m
        if m == 0: return n

        memo = [[0 for i in range(n + 1)] for i in range(m + 1)]
        memo[-1] = list(range(n, -1, -1))
        for i in range(m + 1):
            memo[i][-1] = m - i
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[j] == word2[i]:
                    memo[i][j] = memo[i + 1][j + 1]
                else:
                    memo[i][j] = 1 + min(min(memo[i + 1][j], memo[i+1][j+1]), memo[i][j+1])
                # print(f'updated {i}, {j} to value {memo[i][j]}')
        # print(memo)
        return memo[0][0]

