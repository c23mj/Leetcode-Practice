class UnionFind:
    def __init__(self, count: int):
        self.parent = [x for x in range(count)]
        self.rank = [0 for i in range(count)]

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # path compression
        return self.parent[x]

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)
        # union based on node with lower rank
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootY] < self.rank[rootX]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        UF = UnionFind(len(edges))
        
        for a, b in edges:
            if UF.find(a - 1) == UF.find(b - 1):
                return [a, b]
            UF.union(a - 1, b - 1)

        return [-1, -1]

 