class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[0 if i == j else float('inf') for i in range(n)] for j in range(n)]
        for flight in flights:
            u, v, price = flight
            graph[u][v] = price
        
        
        # memo[i][j]: cost of path from src to node j within i stops
        memo = [[float('inf')] * n for _ in range(k + 2)]
        memo[0][src] = 0
        print(memo)
        for i in range(k + 1):
            for j in range(n):
                if memo[i][j] != float('inf'):
                    for k in range(n):
                        memo[i+1][k] = min(memo[i+1][k], memo[i][j] + graph[j][k])
                        
                # print(f"after checking {j}, next memo row is {memo[i + 1]}")
        # print(memo)
        return memo[-1][dst] if memo[-1][dst] != float('inf') else -1
        
