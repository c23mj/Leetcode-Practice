class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nextLeft, nextRight = [-1] * n, [n] * n
        # approach - stack should be in increasing order, pop until you find something smaller.
        stack = deque()
        for i in range(n):
            height = heights[i]
            while stack and height <= stack[-1][1] :
                stack.pop()
            if stack:
                nextLeft[i] = stack[-1][0]
            stack.append([i, height])

        stack = deque()

        for i in range(n - 1, -1, -1):
            height = heights[i]
            while stack and height <= stack[-1][1] :
                stack.pop()
            if stack:
                nextRight[i] = stack[-1][0]
            stack.append([i, height])
            
        maxRect = float('-inf')
        for i in range(n):
            # print(f'l: {nextLeft[i]}, r: {nextRight[i]}, height: {heights[i]}')
            maxRect = max(maxRect, heights[i] * (nextRight[i] - nextLeft[i] - 1))

        return maxRect

