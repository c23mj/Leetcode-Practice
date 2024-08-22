from collections import defaultdict
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def adjs(r: int, c: int):
            validAdjs = []
            for dx, dy in d:
                a, b = r + dx, c + dy
                if 0 <= a < m and 0 <= b < n and grid[a][b] == 0:
                    grid[a][b] = -1
                    validAdjs.append((a, b))
            return validAdjs
        
        def bfs(r: int, c: int) -> int:
            grid[r][c] = -1
            frontier = deque([(r, c)])
            closed = True
            while frontier:
                a, b = frontier.popleft()
                if a == 0 or a == m - 1 or b == 0 or b == n - 1:
                    closed = False
                frontier.extend(adjs(a, b))
            return int(closed)
        
        closedIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    closedIslands += bfs(i, j)
        return closedIslands
                    