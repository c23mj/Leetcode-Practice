class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            lHeight, rHeight = height[l], height[r]
            area = max(area, min(lHeight, rHeight) * (r - l))
            if lHeight < rHeight:
                l += 1
            else:
                r -= 1
        return area
