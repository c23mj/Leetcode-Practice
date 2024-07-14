class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # print(f"calling subsests with { nums }")
        if not nums:
            return [[]]
        subs = self.subsets(nums[1:])
        # print(f"subs returns {subs}")
        return [[nums[0]] + sub for sub in subs] + subs