class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # print(math.isqrt(c))
        # return False
        for i in range(math.isqrt(c) + 1):
            if (c - i**2) == math.isqrt(c - i**2) ** 2:
                return True
        return False
        #     if 