class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def countIslands():
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
                while frontier:
                    a, b = frontier.popleft()
                    frontier.extend(get_adjs(a, b))
            
            count = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in seen:
                        bfs(i, j)
                        count += 1
            return count

       
        if countIslands() != 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if countIslands() != 1: return 1
                    grid[i][j] = 1
        return 2
        


            
