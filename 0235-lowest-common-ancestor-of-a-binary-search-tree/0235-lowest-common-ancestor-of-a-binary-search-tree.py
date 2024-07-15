# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque()
        queue.append(root);
        i = 0
        # lowest = root
        while(queue):
            for i in range(len(queue)):
                curr = queue.popleft()
                if not curr:
                    continue
                print(curr.val)
                if curr.val == p.val or curr.val == q.val:
                    return curr
    
                if p.val > curr.val and q.val > curr.val:
                    queue.append(curr.right)

                elif p.val < curr.val and q.val < curr.val:
                    queue.append(curr.left)

                else:
                    return curr
                
