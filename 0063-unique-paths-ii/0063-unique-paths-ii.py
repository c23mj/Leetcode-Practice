class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0] * n for _ in range(m)]
        # print(obstacleGrid)
        memo[0][0] = 1
        for i in range(m):
            for j in range(n):
                # print(f'i, j: {(i, j)}')
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0:
                    memo[i][j] += memo[i-1][j]
                if j > 0:
                    memo[i][j] += memo[i][j-1]
            
        return memo[-1][-1]