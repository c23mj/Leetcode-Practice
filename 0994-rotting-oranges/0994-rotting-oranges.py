from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        frontier = deque()
        # adjs for bfs
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def adjs(time: int, r: int, c: int):
            validAdjs = []
            for dx, dy, in d:
                a, b = r + dx, c + dy
                if 0 <= a < m and 0 <= b < n and grid[a][b] == 1 and (a, b) not in seen:
                    seen.add((a, b))
                    validAdjs.append((time + 1, a, b))
            return validAdjs

        totalOranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    totalOranges += 1
                    if grid[i][j] == 2:
                        frontier.append((0, i, j)) # time, r , c
                        seen.add((i, j))

        time = 0
        while frontier:
            time, r, c = frontier.popleft()
            frontier.extend(adjs(time, r, c))
        return time if len(seen) == totalOranges else -1
