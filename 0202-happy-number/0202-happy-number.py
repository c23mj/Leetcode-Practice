class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while n > 1:
            temp = 0
            while n > 0:
                temp += (n % 10) ** 2
                n //= 10
            if temp in seen:
                return False
            else:
                seen.add(temp)
                n = temp
        return True