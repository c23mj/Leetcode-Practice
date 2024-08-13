class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recurse(x: float, n: int):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = recurse(x * x, n //2)
            return x * res if n % 2 == 1 else res
        abs_pow = recurse(x, abs(n))
        return abs_pow if n > 0 else 1.0/abs_pow
        
            
            