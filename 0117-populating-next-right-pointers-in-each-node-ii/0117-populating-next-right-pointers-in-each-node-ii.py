"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = []
        q.append(root)
        dummy = Node(-999)
        while q:
            length = len(q)
            prev = dummy
            for _ in range(length):
                p = q.pop(0)
                if p.left:
                    q.append(p.left)
                    prev.next = p.left
                    prev = prev.next
                if p.right:
                    q.append(p.right)
                    prev.next = p.right
                    prev = prev.next
        
        return root
        