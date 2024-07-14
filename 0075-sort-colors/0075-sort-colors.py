class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, m, r = 0, 0, len(nums) - 1
        while m <= r:
            match nums[m]:
                case 0:
                    nums[m] = nums[l]
                    nums[l] = 0
                    l += 1
                    m += 1
                case 1:
                    m += 1
                case _:
                    nums[m] = nums[r]
                    nums[r] = 2
                    r -= 1
        
