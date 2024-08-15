class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # S0, S1, S2 -> can buy, can sell, cooldown
        n = len(prices)
        memo = [[0 for i in range(n)] for j in range(3)]
        memo[1][0] = -prices[0]
        for i in range(1, n):
            memo[0][i] = max(memo[0][i-1], memo[2][i-1])
            memo[1][i] = max(memo[1][i-1], memo[0][i-1] - prices[i])
            memo[2][i] = memo[1][i-1] + prices[i]
        return max(memo[0][-1], memo[1][-1], memo[2][-1])