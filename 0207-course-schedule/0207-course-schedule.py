from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for course, prereq in prerequisites:
            in_degree[prereq] # access, so the default dictionary creates a value
            in_degree[course] += 1
            graph[prereq].append(course)
        
        frontier = deque([key for key in in_degree.keys() if in_degree[key] == 0])
        topo_count = 0
        while frontier:
            curr = frontier.popleft()
            topo_count += 1
            for adj in graph[curr]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    frontier.append(adj)
        return topo_count == len(in_degree)
                
            
        
            
        # attempt topo sort to find a cycle
        