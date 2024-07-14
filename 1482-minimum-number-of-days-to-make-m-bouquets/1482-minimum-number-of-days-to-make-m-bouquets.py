from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1

        def minHelper(val: int) -> bool:
            i, count = 0, 0
            while i <= n - k:
                if bloomDay[i] <= val:
                    tmp = i
                    while i < tmp + k:
                        if bloomDay[i] > val:
                            break
                        i += 1

                    if i == tmp + k:
                        count += 1
                else:
                    i += 1
            return count >= m


        res, low, high = -1, 1, max(bloomDay)

        while low <= high:
            mid = (low + high) // 2
            if minHelper(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
