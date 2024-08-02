class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return True
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = sum(matrix, [])
        return self.search(flattened, target)