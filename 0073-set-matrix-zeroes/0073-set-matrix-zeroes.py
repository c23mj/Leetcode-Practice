class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        rows, cols = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            matrix[row] = [0] * n

        for col in cols:
            for i in range(m):
                matrix[i][col] = 0
        
        """
        Do not return anything, modify matrix in-place instead.
        """