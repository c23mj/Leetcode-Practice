class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf')] * (amount + 1)
        memo[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                memo[i] = min(memo[i], memo[i - coin] + 1)
        return memo[-1] if memo[-1] != float('inf') else -1