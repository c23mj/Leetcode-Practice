class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prevMax = 0 # max cont subarray up to n, or 0 if max cont subarray is negative
        res = float('-inf')
        for num in nums:
            res = max(res, prevMax + num)
            prevMax = max(prevMax + num, 0)
        return res
            
        