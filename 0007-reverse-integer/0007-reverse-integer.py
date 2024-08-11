class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
#     Repeated division sol
#         res = 0
#         while x:
#             dig = int(math.fmod(x, 10))
#             x = int(x / 10)
#             if res > MAX_INT // 10 or (res == MAX_INT // 10 and dig > MAX_INT % 10) or \
#                res < MIN_INT // 10 or (res == MIN_INT // 10 and dig < MIN_INT % 10):
#                 return 0
#             res = res * 10 + dig
#         return res

#     String manipulation sol
        rev_string = str(x)[::-1]
        if x < 0:
            rev_string = '-' + rev_string[:-1]
        res = int(rev_string)
        return 0 if res > MAX_INT or res < MIN_INT else res
                