class Solution(object):
    def numMagicSquaresInside(self, grid):
        def checkMagicSquare(r: int, c: int):
            nonlocal grid
            nums, sums = set(), set()
            
            for i in range(r, r+3):
                nums.update(grid[i][c:c+3])
                sums.add(sum(grid[i][c:c+3]))
                            
            for j in range(c, c+3):
                sums.add(sum(grid[i][j] for i in range(r, r+3)))

            sums.add(sum(grid[r + i][c + i] for i in range(3)))
            sums.add(sum(grid[r + i][c + 2 - i] for i in range(3)))
            return len(sums) == 1 and nums == set(range(1, 10))
        
        total = 0
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                if checkMagicSquare(r, c):
                    total += 1
        return total