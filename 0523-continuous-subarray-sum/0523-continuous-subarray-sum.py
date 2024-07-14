class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # if len()
        n = len(nums)
        prefixSums = [-1] * n
        prefixSums[0] = nums[0] % k
        for i in range(1, n):
            prefixSums[i] = (prefixSums[i - 1] + nums[i]) % k

        prev = prefixSums[0]
        seen = set()
        for i in range(1, n):
            curr = prefixSums[i]
            if curr == 0 or curr in seen:
                return True
            seen.add(prev)
            prev = curr
        return False

        # return (len(set(prefixSums)) < len(prefixSums)) or (0 in set(prefixSums[1:]))
