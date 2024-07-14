class Solution:
    def trap(self, height: List[int]) -> int:
        rightHeights = deque([(len(height) - 1, height[-1])])
        for i in range(len(height) - 2, -1, -1):
            if height[i] > rightHeights[-1][1]:
                rightHeights.append((i, height[i]))
        
        maxLeft = height[0]
        totalWater = 0
        for i in range(1, len(height) - 1):
            if i > rightHeights[-1][0]:
                rightHeights.pop()
            totalWater += max(0, min(maxLeft, rightHeights[-1][1]) - height[i])
            maxLeft = max(maxLeft, height[i])
        return totalWater