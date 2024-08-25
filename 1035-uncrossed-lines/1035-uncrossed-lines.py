class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        memo = {}
        def countAtIndices(i: int, j: int):
            if i >= m or j >= n:
                return 0
            if (i, j) not in memo:
                if nums1[i] == nums2[j]:
                    memo[(i, j)] = 1 + countAtIndices(i+1, j+1)
                else:
                    memo[(i, j)] = max(countAtIndices(i, j + 1), countAtIndices(i + 1, j))
            return memo[(i, j)]
        return countAtIndices(0, 0)