class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        # space-optimized 2n dp
        m, n = len(nums1), len(nums2)
        prev = [0] * (n + 1)
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr
        return curr[-1]      
                    

        # iterative mn dp
        # m, n = len(nums1), len(nums2)
        # memo = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if nums1[i - 1] == nums2[j - 1]:
        #             memo[i][j] = 1 + memo[i-1][j-1]
        #         else:
        #             memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        # return memo[-1][-1]        
                    
        
        # m, n = len(nums1), len(nums2)
        # memo = {}
        # def countAtIndices(i: int, j: int):
        #     if i >= m or j >= n:
        #         return 0
        #     if (i, j) not in memo:
        #         if nums1[i] == nums2[j]:
        #             memo[(i, j)] = 1 + countAtIndices(i+1, j+1)
        #         else:
        #             memo[(i, j)] = max(countAtIndices(i, j + 1), countAtIndices(i + 1, j))
        #     return memo[(i, j)]
        # return countAtIndices(0, 0)