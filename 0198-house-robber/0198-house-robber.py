class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0 for i in range(len(nums) + 1)]
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            memo[i + 1] = max(memo[i], memo[i - 1] + nums[i])
        return memo[-1]