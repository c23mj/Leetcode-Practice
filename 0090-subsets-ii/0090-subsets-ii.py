class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sub = []
        def subsets(idx: int):
            if idx >= len(nums):
                res.append(sub[:])
                return

            # use it    
            sub.append(nums[idx])
            subsets(idx + 1)

            sub.pop()
            # don't use it, but skip until no more duplicates to prevent extra dupes
            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1
            subsets(idx + 1) 

        subsets(0)
        return res
                