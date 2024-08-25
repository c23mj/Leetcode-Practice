from collections import defaultdict
import heapq

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v, dist in roads:
            graph[u][v] = dist
            graph[v][u] = dist
        
        seen = set()
        minEdge = float('inf')
        frontier = deque([1])
        while frontier:
            curr = frontier.popleft()
            minEdge = min(minEdge, *graph[curr].values())
            newCities = [adj for adj in graph[curr] if adj not in seen]
            frontier.extend(newCities)
            seen.update(newCities)
        return minEdge
            
            
            
            
        