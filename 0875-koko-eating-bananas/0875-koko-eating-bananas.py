import numpy as np
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles_arr = np.array(piles)
        l, r, res = 1, max(piles), -1
        while l <= r:
            mid = (l + r) // 2
            if np.sum(np.ceil(piles_arr / mid)) <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1 
        return res
            
            