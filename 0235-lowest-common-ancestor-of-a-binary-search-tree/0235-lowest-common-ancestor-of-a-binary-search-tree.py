# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        frontier = deque([root])
        while frontier:
            curr = frontier.popleft() 
            if curr.val == p.val or curr.val == q.val or \
               q.val < curr.val < p.val or p.val < curr.val < q.val:
                return curr
            if p.val < curr.val and q.val < curr.val:
                frontier.append(curr.left)
            else:
                frontier.append(curr.right)
        return None

        
        
        
        
