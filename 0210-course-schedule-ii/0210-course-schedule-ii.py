class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        reqGraph = defaultdict(list)
        for c, p in prerequisites:
            reqGraph[p].append(c)
        
        in_degree = defaultdict(int)
        for i in range(numCourses):
            for el in reqGraph[i]:
                in_degree[el] += 1

        out = []
        zero_degree = deque([i for i in range(numCourses) if in_degree[i] == 0])
        while zero_degree:
            curr = zero_degree.popleft()
            out.append(curr)

            for adj in reqGraph[curr]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    zero_degree.append(adj)
       
        if len(out) == numCourses: return out
        return []
