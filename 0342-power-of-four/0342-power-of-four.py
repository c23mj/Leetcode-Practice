import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        roundedLog4 = int(math.log(n, 4))
        return 4 ** roundedLog4 == float(n)