# from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachable = set()
        for edge in edges:
            reachable.add(edge[1])
        return list(set(range(n)) - reachable)
