class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        maxScore = 0
        runningSum = 0
        for i in range(len(nums)):
            runningSum += nums[i]
            if runningSum <= 0:
                return maxScore
            maxScore += 1

        return maxScore