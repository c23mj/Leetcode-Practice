class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = currentMax = nextMax = 0
        for i in range(n - 1):
            nextMax = max(nextMax, i + nums[i])
            if i == currentMax:
                jumps += 1
                currentMax = nextMax
        return jumps
    