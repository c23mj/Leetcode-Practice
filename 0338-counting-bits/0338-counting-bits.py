class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            if i % 2 == 0:
                output[i] = output[i//2]
            else:
                output[i] = output[i-1] + 1
        return output
