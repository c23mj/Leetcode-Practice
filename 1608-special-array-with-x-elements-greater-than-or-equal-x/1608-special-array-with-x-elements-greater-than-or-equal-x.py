class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        if nums[-1] >= n:
            return n
        for i in range(n - 1):
            if nums[i] >= i + 1 and nums[i + 1] < i + 1:
                return i + 1
        return -1


        # [4 4 3 0 0]
        # asdasldasldas
        # asdlasdjl