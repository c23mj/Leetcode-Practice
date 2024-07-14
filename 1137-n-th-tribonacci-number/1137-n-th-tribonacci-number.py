class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        i, j, k = 0, 1, 1
        for _ in range(n - 2):
            temp = i + j + k
            i = j 
            j = k
            k = temp
        return k