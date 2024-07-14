# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        curr = root
        stack, lst = [], []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            lst.append(curr.val)
            curr = curr.right

        currSum = 0
        for i in range(len(lst) - 1, -1, -1):
            lst[i] += currSum
            currSum = lst[i]
        
        i = 0
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            curr.val = lst[i]
            i += 1
            curr = curr.right


        return root

            

