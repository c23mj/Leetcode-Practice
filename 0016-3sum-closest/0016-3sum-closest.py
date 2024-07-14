class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        ans = 0
        for i in range(len(nums) - 1):
            first = nums[i]
            small = i + 1
            big = len(nums) - 1
            while small < big:
                currSum = first + nums[small] + nums[big]
                if abs(currSum - target) < diff:
                    ans = currSum
                    diff = abs(currSum - target)
                if currSum < target:
                    small += 1
                elif currSum > target:
                    big -= 1
                else:
                    return target
        return ans