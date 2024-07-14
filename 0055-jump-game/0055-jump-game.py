class Solution:
    def canJump(self, nums: List[int]) -> bool:
        best = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            # print(f'best: {best}, i + nums[i]: {i + nums[i]}')
            if i + nums[i] >= best:
                best = i
        return best == 0