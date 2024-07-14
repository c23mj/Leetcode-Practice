class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        out = ([],[])
        for i in nums:
            if i % 2 == 0:
                out[0].append(i)
            else:
                out[1].append(i)
        return out[0] + out[1]