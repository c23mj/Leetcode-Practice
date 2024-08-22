class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(values)):
            dividend, divisor = equations[i]
            value = values[i]
            graph[dividend].append((divisor, value))
            graph[divisor].append((dividend, 1.0/value))
            
        res = []
        for query in queries:
            dividend, divisor = query
            if dividend not in graph or divisor not in graph:
                res.append(-1.0)
                continue
            if dividend == divisor:
                res.append(1.0)
                continue
            found = False
            seen = {dividend}
            frontier = deque([(dividend, 1.0)])
            while frontier:
                curr, val = frontier.popleft()
                if curr == divisor:
                    res.append(val)
                    found = True
                    break
                for adj, cost in graph[curr]:
                    if adj not in seen:
                        seen.add(adj)
                        frontier.append((adj, val * cost))
            if not found:
                res.append(-1.0)
        return res
                    
        