class Solution:
    def numTrees(self, n: int):
        a = [-1] * 20
        a[0] = 1
        a[1] = 1
        def helper(n: int) -> int:
            if a[n] != -1:
                return a[n]
            total = 0
            for i in range(n):
                total += helper(i) * helper(n - i - 1)
            a[n] = total
            return total
        return helper(n)