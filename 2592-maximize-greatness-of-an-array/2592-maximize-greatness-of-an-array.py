class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count, big, small = 0, 0, 1
        while small < len(nums):
            if nums[big] > nums[small]:
                count += 1
                big += 1
                small += 1
            else:
                small += 1
        return count