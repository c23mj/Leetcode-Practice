from collections import deque
class Solution:
    adjs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def isValid(r, c):
            return 0 <= r < m and 0 <= c < n

        oceanGrid = [[0 for i in range(n)] for _ in range(m)]
        # print(oceanGrid)
        pacific = [(0, i) for i in range(n)] + [(j, 0) for j in range(m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(j, n - 1) for j in range(m)]
        # print(pacific)
        # print(atlantic)
        frontier = deque(pacific)
        visited = set(pacific)
        while frontier:
            currRow, currCol = frontier.popleft()
            oceanGrid[currRow][currCol] += 1 # pacific + 1
            currVal = heights[currRow][currCol]
            for adj in self.adjs:
                r, c = currRow + adj[0], currCol + adj[1]
                if isValid(r, c) and currVal <= heights[r][c] and (r, c) not in visited:
                    visited.add((r, c))
                    frontier.append((r, c))

        frontier = deque(atlantic)
        visited = set(atlantic)
        while frontier:
            currRow, currCol = frontier.popleft()
            oceanGrid[currRow][currCol] += 2 # atlantic + 2
            currVal = heights[currRow][currCol]
            for adj in self.adjs:
                r, c = currRow + adj[0], currCol + adj[1]
                if isValid(r, c) and currVal <= heights[r][c] and (r, c) not in visited:
                    visited.add((r, c))
                    frontier.append((r, c))
        
        oceanGrid[0][0] = oceanGrid[0][0] - 1
        oceanGrid[m-1][n-1] = oceanGrid[m-1][n-1] - 2
        output = []
        for i in range(m):
            for j in range(n):
                if oceanGrid[i][j] == 3:
                    output.append([i, j])
        # print(output)
        return output            



