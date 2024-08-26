class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def adjs(r: int, c: int):
            validAdjs = []
            adjCount = 0
            for dx, dy in d:
                a, b = r + dx, c + dy
                if 0 <= a < m and 0 <= b < n:
                    if grid[a][b] == 1:
                        grid[a][b] = -1
                        validAdjs.append((a, b))
                        adjCount += 1
                    elif grid[a][b] == -1:
                        adjCount += 1
            return validAdjs, adjCount
            
        def bfs(r: int, c: int):
            grid[r][c] = -1
            perimeter = 0
            frontier = deque([(r, c)])
            while frontier:
                a, b = frontier.popleft()
                validAdjs, count = adjs(a, b)
                perimeter += 4 - count
                frontier.extend(validAdjs)
            return perimeter
            
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return bfs(i, j)