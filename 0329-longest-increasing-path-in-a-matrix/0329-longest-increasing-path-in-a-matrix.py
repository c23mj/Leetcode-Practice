class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = {}
        def dfs(r: int, c: int, prevVal: int) -> int:
            if 0 <= r < m and 0 <= c < n and matrix[r][c] > prevVal:
                if (r, c) in memo:
                    return memo[(r, c)]
                maxPath = 1 # base Node
                maxPath = max(maxPath, 1 + dfs(r + 1, c, matrix[r][c]))
                maxPath = max(maxPath, 1 + dfs(r - 1, c, matrix[r][c]))
                maxPath = max(maxPath, 1 + dfs(r, c + 1, matrix[r][c]))
                maxPath = max(maxPath, 1 + dfs(r, c - 1, matrix[r][c]))
                memo[(r, c)] = maxPath
                return maxPath
            return 0

        for i in range(m):
            for j in range(n):
                dfs(i, j, -1)
        return max(memo.values())

                