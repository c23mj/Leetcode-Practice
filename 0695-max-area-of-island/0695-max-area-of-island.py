class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        
        # adj logic
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def get_adjs(r: int, c: int):
            validAdjs = []
            for dx, dy in d:
                a, b = r + dx, c + dy
                if 0 <= a < m and 0 <= b < n and (a, b) not in seen and grid[a][b] == 1:
                    seen.add((a, b))
                    validAdjs.append((a, b))
            return validAdjs
        # end adj logic
            
        
        def bfs(r: int, c: int):
            seen.add((r, c))
            frontier = deque([(r, c)])
            count = 0
            while frontier:
                a, b = frontier.popleft()
                count += 1
                frontier.extend(get_adjs(a, b))
            return count
        
        
        maxCount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    maxCount = max(maxCount, bfs(i, j))
        return maxCount
