"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None}
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        for node in oldToNew:
            if node:
                oldToNew[node].next = oldToNew[node.next]
                oldToNew[node].random = oldToNew[node.random]
        return oldToNew[head]