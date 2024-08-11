class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # reversing numbers for ease of multiplication later
        num1 = num1[::-1] 
        num2 = num2[::-1] 

        def singleDigitMultiply(num2digit: int) -> int:
            res = 0
            for i in range(len(num1)):
                res += num2digit * int(num1[i]) * (10 ** i)
            return res
        res = 0
        for i in range(len(num2)):
            res += singleDigitMultiply(int(num2[i])) * (10 ** i)
        return str(res)
        

