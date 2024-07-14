class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjList = defaultdict(list)
        inDegree = defaultdict(int)
        # roots = set(range(n))
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            inDegree[edge[1]] += 1
        
        out = [set() for i in range(n)]
        queue = deque([i for i in range(n) if inDegree[i] == 0])
        while queue:
            vertex = queue.popleft()
            for neighbor in adjList[vertex]:
                out[neighbor].update(out[vertex])
                out[neighbor].add(vertex)
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        return [sorted(list(s)) for s in out]