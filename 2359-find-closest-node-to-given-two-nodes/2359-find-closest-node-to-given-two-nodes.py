class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = dict()
        for i in range(len(edges)):
            if edges[i] != -1:
                adj[i] = edges[i]
        frontier1, seen1 = deque([node1]), {node1}
        frontier2, seen2 = deque([node2]), {node2}
        while frontier1 or frontier2:
            ans = float('inf')
            addto1 = -1
            if frontier1:
                curr1 = frontier1.popleft()
                if curr1 in seen2:
                    ans = min(ans, curr1)
                elif curr1 in adj and adj[curr1] not in seen1:
                    addto1 = adj[curr1]
                    frontier1.append(adj[curr1])
                    
            if frontier2:
                curr2 = frontier2.popleft()
                if curr2 in seen1:
                    ans = min(ans, curr2)
                if curr2 in adj and adj[curr2] not in seen2:
                    seen2.add(adj[curr2])
                    frontier2.append(adj[curr2])
            seen1.add(addto1)
            
            if ans != float('inf'):
                return ans
        return -1
    
