class Solution:
    def reverseBits(self, n: int) -> int:
        # string comprehension
        # return int((str(bin(n))[2:].zfill(32)[::-1]), 2)
        
        # bit manipulation
        res = 0
        for i in range(32):
            nextBit = (n >> i) & 1
            res += (nextBit << (31 - i))
        return res