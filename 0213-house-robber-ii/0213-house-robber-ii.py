class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        memo_one, memo_two = [0 for i in range(n)], [0 for i in range(n)]
        
        # rob houses 1-n-1
        memo_one[1] = nums[0]
        memo_two[1] = nums[1]
        for i in range(2, len(nums)):
            memo_one[i] = max(memo_one[i - 1], memo_one[i - 2] + nums[i - 1])
            memo_two[i] = max(memo_two[i - 1], memo_two[i-2] + nums[i])
                
        return max(memo_one[-1], memo_two[-1])