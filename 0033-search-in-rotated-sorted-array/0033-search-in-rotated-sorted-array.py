class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # try:
        #     return nums.index(target)
        # except ValueError:
        #     return -1
        l, r, pivot = 0, len(nums) - 1, -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                pivot = mid
                l = mid + 1
            else:
                r = mid - 1

        # print(pivot)

        if pivot == -1:
            pivot = len(nums) - 1

        if nums[0] == target:
            return 0
        elif nums[0] < target:
            l, r = 0, pivot
        else:
            l, r = pivot + 1, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
                    