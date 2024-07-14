class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count, n = 0, len(nums)
        for i in range(n):
            if nums[i] % 2 == 1:
                count += 1
            nums[i] = count
        
        count = 0
        prefixCounts = defaultdict(int)
        for el in nums:
            if el == k:
                count += 1
            count += prefixCounts[el - k]
            prefixCounts[el] += 1
        return count