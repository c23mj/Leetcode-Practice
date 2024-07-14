class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            minPrefix = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    minPrefix = max(minPrefix, memo[j])
            memo[i] = minPrefix + 1
        return max(memo)


