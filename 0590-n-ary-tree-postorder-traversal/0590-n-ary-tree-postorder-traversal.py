"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        out = deque()
        frontier = deque([root])
        while frontier:
            curr = frontier.pop()
            out.appendleft(curr.val)
            frontier.extend(curr.children)
        return list(out)