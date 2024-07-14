from collections import defaultdict, deque
import copy
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjGraph = defaultdict(set)
        if n == 0:
            return []
        if n == 1:
            return [0]
        for edge in edges:
            adjGraph[edge[0]].add(edge[1])
            adjGraph[edge[1]].add(edge[0])
        
        frontier = deque([node for node in range(n) if len(adjGraph[node]) == 1])

        while len(adjGraph.keys()) > 2:
            # print(f"frontier: {frontier}")
            roundCount = len(frontier)
            while(roundCount > 0):
                curr = frontier[0]
                frontier.popleft()
                parent = list(adjGraph[curr])[0]
                del adjGraph[curr]
                adjGraph[parent].discard(curr)
                if len(adjGraph[parent]) == 1:
                    frontier.append(parent)
                roundCount -= 1

        return adjGraph.keys()



            # i += 1
            # nodes = adjGraph.keys()
            # if len(nodes) <= 2:
            #     return nodes
            # nextAdj = copy.deepcopy(adjGraph)
            # for node in nodes:
            #     if len(adjGraph[node]) == 1:
            #         # print(f"leaf node: {node}")
            #         del(nextAdj[node])
            #         # print(f"adj: {adjGraph[node]}")
            #         adjSet = list(adjGraph[node])
            #         # print(f"adj set: {adjSet}")
            #         el = adjSet[0]
            #         nextAdj[el].discard(node)
            # adjGraph = nextAdj

