class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # adjacent logic
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def adjs(r, c):
            validAdjs = []
            for dx, dy in d:
                a, b = r + dx, c + dy
                if 0 <= a < n and 0 <= b < n:
                    validAdjs.append((a, b))
            return validAdjs
        
        dist = [[float('inf') for i in range(n)] for j in range(n)]
        dist[0][0] = grid[0][0]
        # print(dist)
        
        # struct: (cost, r, c)
        pq = [(dist[0][0], 0, 0)]
        while pq:
            cost, row, col = heapq.heappop(pq)
            if cost < dist[row][col]:
                dist[row][col] = cost
            for adjRow, adjCol in adjs(row, col):
                adjCost = max(cost, grid[adjRow][adjCol])
                if adjCost < dist[adjRow][adjCol]:
                    dist[adjRow][adjCol] = adjCost
                    heapq.heappush(pq, (adjCost, adjRow, adjCol))
        # print(dist)
        return dist[-1][-1]
        
        