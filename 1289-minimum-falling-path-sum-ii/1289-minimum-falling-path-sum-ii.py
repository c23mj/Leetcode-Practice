import copy
import heapq
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def twoSmallest(l: List[int]):
            smallest = float('inf')
            second_smallest = float('inf')
            smallest_index = -1
            second_smallest_index = -1

            # Iterate through the list
            for index, value in enumerate(l):
                if value < smallest:
                    second_smallest, second_smallest_index = smallest, smallest_index
                    smallest, smallest_index = value, index
                elif value < second_smallest:
                    second_smallest, second_smallest_index = value, index
            return ((smallest, smallest_index), (second_smallest, second_smallest_index))

        memo = copy.deepcopy(grid)
        # print(memo)
        for i in range(1, len(grid)):
            rowMin = twoSmallest(memo[i-1])
            for j in range(len(grid)):    
                memo[i][j] += rowMin[0][0] if rowMin[0][1] != j else rowMin[1][0]

        # print(memo)
        return min(memo[len(grid)-1])