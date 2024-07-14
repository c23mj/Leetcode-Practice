class DisjointSet:
    def __init__(self, size):
        self.parents = list(range(size))
        self.merges = 0

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, i, j):
        irep, jrep = self.find(i), self.find(j)
        if irep == jrep:
            return False
        self.merges += 1
        self.parents[irep] = jrep
        return True
        
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edgeCount = 0
        splitEdges = [[], [], []]
        for edge in edges:
            splitEdges[edge[0] - 1].append(edge)

        alice, bob = DisjointSet(n), DisjointSet(n)
        # print(splitEdges)
        for edge in splitEdges[2]:
            a = alice.union(edge[1] - 1, edge[2] - 1)
            b = bob.union(edge[1] - 1, edge[2] - 1)
            if a or b:
                edgeCount += 1

        for edge in splitEdges[1]:
            if bob.union(edge[1] - 1, edge[2] - 1):
                edgeCount += 1

        for edge in splitEdges[0]:
            if alice.union(edge[1] - 1, edge[2] - 1):
                edgeCount += 1
        
        # print(alice.merges)
        # print(bob.merges)
        if alice.merges < n - 1 or bob.merges < n - 1:
            return -1
        return len(edges) - edgeCount
 
