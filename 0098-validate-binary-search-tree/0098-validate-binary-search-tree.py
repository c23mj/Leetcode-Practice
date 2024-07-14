# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getInorder(self, root: Optional[TreeNode], out):
        if not root:
            return []
        self.getInorder(root.left, out)
        out.append(root.val)
        self.getInorder(root.right, out)
        return out

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inOrder = self.getInorder(root, [])
        # print(inOrder)
        for i in range(1, len(inOrder)):
            if inOrder[i] <= inOrder[i-1]:
                return False
        return True