class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        numGrid = [[0 for _ in range(3 * n)] for _ in range(3 * n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '\\':
                    numGrid[3 * i][3 * j] = 1
                    numGrid[3 * i + 1][3 * j + 1] = 1
                    numGrid[3 * i + 2][3 * j + 2] = 1

                elif grid[i][j] == '/':
                    numGrid[3 * i + 2][3 * j] = 1
                    numGrid[3 * i + 1][3 * j + 1] = 1
                    numGrid[3 * i][3 * j + 2] = 1

        seen = set()

        def bfs(r: int, c: int) -> None:
            adjDirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            def adjs(r, c):
                validAdjs = []
                for dx, dy in adjDirs:
                    a, b = r + dx, c + dy
                    if 0 <= a < 3 * n and 0 <= b < 3 * n and numGrid[a][b] == 0 and (a, b) not in seen:
                        validAdjs.append((a, b))
                        seen.add((a, b))
                # print(f"valid adjs for {r}, {c}: {validAdjs}")
                return validAdjs
            frontier = deque([(r, c)])
            while frontier:
                a, b = frontier.popleft()
                frontier.extend(adjs(a, b))
            return

        regionCount = 0
        for i in range(3 * n):
            for j in range(3 * n):
                if numGrid[i][j] == 0 and (i, j) not in seen:
                    seen.add((i, j))
                    bfs(i, j)
                    # print(f"new region found! new seen: {seen}")
                    regionCount += 1


        return regionCount
                    