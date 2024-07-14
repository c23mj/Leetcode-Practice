# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodesHelper(self, root: TreeNode, largest: int):
        if not root: return 0
        if largest <= root.val:
            return 1 + self.goodNodesHelper(root.left, root.val) + self.goodNodesHelper(root.right, root.val)
        return self.goodNodesHelper(root.left, largest) + self.goodNodesHelper(root.right, largest)
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, float('-inf'))
        
        