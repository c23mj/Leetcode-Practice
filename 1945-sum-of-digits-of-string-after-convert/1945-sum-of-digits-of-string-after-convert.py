class Solution:
    def getLucky(self, s: str, k: int) -> int:
        unconverted = []
        for char in s:
            unconverted.append(ord(char) - ord('a') + 1)
        
        res = int(''.join(map(str, unconverted)))
        for i in range(k):
            res = sum(int(digit) for digit in str(res))
        return res
            