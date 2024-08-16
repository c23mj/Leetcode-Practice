import heapq
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mins, maxes = [], []
        for i in range(2):
            heapq.heappush(mins, (-arrays[i][0], i))
            heapq.heappush(maxes, (arrays[i][-1], i))
                                   
        # print(f"mins, maxes: {mins}, {maxes}")
        for i in range(2, len(arrays)):
            heapq.heappushpop(mins, (-arrays[i][0], i))     
            heapq.heappushpop(maxes, (arrays[i][-1], i))
        
#         print(mins)
#         print(maxes)
        
        if mins[1][1] != maxes[1][1]:
            return maxes[1][0] + mins[1][0]
        return max(maxes[1][0] + mins[0][0], maxes[0][0] + mins[1][0])
        