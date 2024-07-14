import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        phi = (1 + np.sqrt(5)) / 2
        psi = (1 - np.sqrt(5)) / 2
        return int((phi**(n+1) - psi**(n+1)) / np.sqrt(5))