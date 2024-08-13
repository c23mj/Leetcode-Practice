from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        def adjs(r: int, c: int):
            validAdjs = []
            for dx, dy in d:
                a, b = r + dx, c + dy
                if 0 <= a < m and 0 <= b < n and grid[a][b] == '1' and (a, b) not in seen:
                    seen.add((a, b))
                    validAdjs.append((a, b))
            return validAdjs            
            
        def bfs(r: int, c: int):
            seen.add((r, c))
            frontier = deque([(r, c)])
            while frontier:
                a, b = frontier.popleft()
                # print(f"popped: {a, b}")
                frontier.extend(adjs(a, b))
            # print(f"bfs complete. seen: {seen}")
            
         
        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    bfs(i, j)
                    island_count += 1
        return island_count
                    
        
        