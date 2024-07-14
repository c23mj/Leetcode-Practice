# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBalancedFromSorted(self, lst: List[int]):
        if not lst:
            return None
        mid = len(lst)//2
        return TreeNode(lst[mid], self.createBalancedFromSorted(lst[:mid]), self.createBalancedFromSorted(lst[mid+1:]))
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        curr = root
        stack, lst = [], []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            lst.append(curr.val)
            curr = curr.right
        return self.createBalancedFromSorted(lst)