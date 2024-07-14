# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        d1, d2 = deque([p]), deque([q])
        while d1:
            curr1, curr2 = d1.pop(), d2.pop()
            if (not curr1 and curr2) or (curr1 and not curr2):
                return False
            if not curr1 and not curr2:
                continue
            if curr1.val != curr2.val:
                return False
            d1.extend([curr1.left, curr1.right])
            d2.extend([curr2.left, curr2.right])
        return True
