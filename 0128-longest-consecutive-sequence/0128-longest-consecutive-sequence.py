class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        currConsec = 1
        maxConsec = float('-inf')
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                currConsec += 1
                print(currConsec)
            else:
                maxConsec = max(maxConsec, currConsec)
                currConsec = 1
                
        maxConsec = max(maxConsec, currConsec)
        return maxConsec
        