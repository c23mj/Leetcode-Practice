class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        lefts = nums[:4]
        rights = nums[-4:][::-1]
        best = float("inf")
        for i in range(len(lefts)):
            for j in range(len(rights) - i):
                # print(f"testing {i}, {j}: {abs(nums[j] - nums[i])}")
                best = min(best, abs(lefts[j] - rights[i]))
        # print(lefts)
        # print(rights)

        return best