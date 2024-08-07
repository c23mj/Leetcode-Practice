# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        levels = []
        nextLevel = [root]
        while nextLevel:
            frontier = deque(nextLevel)
            nextLevel = []
            levels.append([])
            while frontier:
                curr = frontier.popleft()
                levels[-1].append(curr.val)
                if curr.left:
                    nextLevel.append(curr.left)
                if curr.right:
                    nextLevel.append(curr.right)
        return [level[-1] for level in levels]
                
    
        