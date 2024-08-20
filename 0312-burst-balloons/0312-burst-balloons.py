class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def solve(i: int, j: int):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            maxCost = 0
            for k in range(i, j + 1):
                cost = nums[i - 1] * nums[k] * nums[j + 1]
                cost += solve(i, k -1)
                cost += solve(k + 1, j)
                maxCost = max(maxCost, cost)
            memo[(i, j)] = maxCost
            return maxCost
        return solve(1, len(nums) - 2)
        
                