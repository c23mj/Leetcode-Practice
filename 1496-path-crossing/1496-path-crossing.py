class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = {(0, 0)}
        currX, currY = 0, 0
        dirs = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for d in path:
            dx, dy = dirs[d]
            currX, currY = currX + dx, currY + dy
            if (currX, currY) in seen:
                return True
            seen.add((currX, currY))

        return False