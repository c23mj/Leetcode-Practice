class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][n - 1 - i]
                matrix[n - 1 - j][n - 1 - i] = tmp
        
        for i in range(n//2):
            tmp = matrix[i]
            matrix[i]= matrix[n - 1 - i]
            matrix[n - 1 - i] = tmp
        
