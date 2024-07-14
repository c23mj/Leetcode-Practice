class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        nums.sort()
        patches, currSum, i = 0, 0, 0
        while i < len(nums) and currSum < n:
            if nums[i] <= currSum + 1:
                currSum += nums[i]
                i += 1
            else:
                patches += 1
                currSum += currSum + 1
        
        if i == len(nums) and currSum < n:
            while currSum < n:
                patches += 1
                currSum += currSum + 1
        return patches