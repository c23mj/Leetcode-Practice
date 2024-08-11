class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [float('inf') for _ in range(n)]
        memo[-1] = 0
        for i in range(n - 2, -1, -1):
            memo[i] = 1 + min(memo[i: min(n, i + nums[i] + 1)])
        print(memo)
        return memo[0]