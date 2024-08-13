"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return

        nodeRefs = {node: Node()}
        frontier = deque([node])
        while frontier:
            currNode = frontier.popleft()
            nodeRefs[currNode].val = currNode.val
            adjs = [neigh for neigh in currNode.neighbors if neigh not in nodeRefs]
            for adj in adjs:
                nodeRefs[adj] = Node()
            frontier.extend(adjs)
        for n in nodeRefs.keys():
            nodeRefs[n].neighbors = [nodeRefs[neigh] for neigh in n.neighbors]
        return nodeRefs[node]


    
        
