class Solution:
    def reverseBits(self, n: int) -> int:
        # print()
        return int((str(bin(n))[2:].zfill(32)[::-1]), 2)