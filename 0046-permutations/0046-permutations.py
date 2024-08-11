class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # with itertools
        # return itertools.permutations(nums)

        # recursively
        # if len(nums) <= 1:
        #     return [nums]
        # res = []
        # for i in range(len(nums)):
        #     res.extend([nums[i]] + perm for perm in self.permute(nums[:i] + nums[i+1:]))
        # return res
              
        # backtracking
        if len(nums) <= 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            skipped = nums.pop(0)
            perms = self.permute(nums)
            res.extend(perm + [skipped] for perm in perms)
            nums.append(skipped)
        return res
            