# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def longestZigZag(self, root):
        # tuple: (TreeNode, int, bool)
        #      ->(Node, len, isLeftChild?)
        if not root: return 0
        longest = 0
        queue = deque([(root.left, 0, True), (root.right, 0, False)])
        while queue:
            curr = queue[0]
            queue.popleft()
            if curr[0] is None:
                longest = max(longest, curr[1])
            elif curr[2] == True:
                queue.extend([(curr[0].right, curr[1] + 1, False), 
                              (curr[0].left, 0, True)])
            else:
                queue.extend([(curr[0].left, curr[1] + 1, True), 
                              (curr[0].right, 0, False)])
        return longest
            

        """
        :type root: TreeNode
        :rtype: int
        """
        