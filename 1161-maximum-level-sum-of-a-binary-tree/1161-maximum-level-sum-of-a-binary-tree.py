# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = []
        q = deque()
        q.append(root)
        while q:
            runningSum = 0
            for i in range(len(q)):
                curr = q.popleft()
                runningSum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            sums.append(runningSum)

        # do an argmax
        max = 0
        for i in range(1, len(sums)):
            if sums[i] > sums[max]:
                max = i
        return max + 1
        