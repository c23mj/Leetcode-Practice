# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        next_level = [root]
        out = []
        frontier = deque()
        while next_level:
            frontier.extend(next_level)
            next_level = []
            out.append([])
            while frontier:
                curr = frontier.popleft()
                out[-1].append(curr.val)
                if curr.left:
                    next_level.append(curr.left)
                if curr.right:
                    next_level.append(curr.right)
        return out
            
                
                
                