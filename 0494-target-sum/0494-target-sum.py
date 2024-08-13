class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = dict()
        def backtrack(idx: int, target: int):
            if (idx, target) in memo:
                return memo[(idx, target)]
            ways = 0
            if idx == len(nums):
                if target == 0:
                    return 1
                else:
                    return 0
            
            ways += backtrack(idx + 1, target - nums[idx])
            ways += backtrack(idx + 1, target + nums[idx])
            memo[(idx, target)] = ways
            return ways
            
        return backtrack(0, target)
   
            