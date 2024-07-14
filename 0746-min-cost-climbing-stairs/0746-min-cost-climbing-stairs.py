class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = cost
        for i in range(2, len(cost)):
            memo[i] += min(memo[i - 1], memo[i - 2])
        return min(memo[-1], memo[-2])