class Solution(object):
    def minFallingPathSum(self, matrix):
        min_sums = matrix
        for i in range(1, len(matrix)):
            for j in range(0, len(matrix[0])):
                min_score = float("inf")
                if j > 0:
                    min_score = min(min_score, min_sums[i - 1][j - 1])
                min_score = min(min_score, min_sums[i-1][j])
                if j < len(matrix[0]) - 1:
                    min_score = min(min_score, min_sums[i-1][j+1])
                min_sums[i][j] = min_score + matrix[i][j]

        return min(min_sums[len(matrix[0]) - 1]) 
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        