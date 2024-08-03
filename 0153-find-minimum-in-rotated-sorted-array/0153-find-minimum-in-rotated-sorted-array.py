class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # first = nums[0]
        while l < r:
            mid = (l + r)  // 2
            if nums[mid] > nums[r]: # left of inflection
                l = mid + 1
            else: # right of inflection
                r = mid
        
        return nums[l]
    