class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        edgeList = defaultdict(set)
        for u, v in edges:
            edgeList[u].add(v)
            edgeList[v].add(u)

        def dfs(curr, parent):
            totalTime = 0
            for child in edgeList[curr]:
                if child == parent:
                    continue
                subTreeTime = dfs(child, curr)
                if subTreeTime > 0 or hasApple[child]:
                    totalTime += subTreeTime + 2
            return totalTime
        
        return dfs(0, -1)