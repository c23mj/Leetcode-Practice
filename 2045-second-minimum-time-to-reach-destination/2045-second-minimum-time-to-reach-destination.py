class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        def calcTime(pathLength):
            nonlocal time, change
            total = 0
            while pathLength:
                phase = total % (change * 2)
                if phase >= change:
                    total += (2 * change - phase)
                total += time
                pathLength -= 1
            return total
        
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        seen = defaultdict(set)
        frontier = deque([(1, 0)])
        bestSol = float("inf")
        while frontier:
            # print(frontier)
            curr, currLength = frontier.popleft()
            if curr == n:
                # print(f"found solution, cost: {currLength}")
                bestSol = min(bestSol, currLength)
                if currLength > bestSol:
                    # print(f"second best currLength: {currLength}")
                    return calcTime(currLength)
            if len(seen[curr]) < 2 and currLength not in seen[curr] and adjList[curr]:
                seen[curr].add(currLength)
                frontier.extend((adj, currLength + 1) for adj in adjList[curr])
        return calcTime(bestSol + 2)            
