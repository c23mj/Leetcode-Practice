class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        total = 0
        for i in range(len(arr) - 1):
            left = 0
            for j in range(i + 1, len(arr)):
                left ^= arr[j - 1]
                right = 0
                for k in range(j, len(arr)):
                    right ^= arr[k]
                    if left == right:
                        total += 1
        return total

