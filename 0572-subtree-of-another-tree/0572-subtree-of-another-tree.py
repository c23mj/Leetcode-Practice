# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEqual(self, s: Optional[TreeNode], t: Optional[TreeNode]):
        if not s: return not t
        if not t: return not s
        return s.val == t.val and self.isEqual(s.left, t.left) and self.isEqual(s.right, t.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return not subRoot
        return self.isEqual(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)