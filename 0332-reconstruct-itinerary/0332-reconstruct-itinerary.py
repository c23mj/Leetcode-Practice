class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:        
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
        for adjList in graph.values():
            adjList.sort(reverse=True)

        itinerary = []
        stack = ['JFK']
        while stack:
            curr = stack[-1]
            if graph[curr]:
                next = graph[curr].pop()
                stack.append(next)
            else:
                itinerary.append(stack.pop())
        return itinerary[::-1]

        


