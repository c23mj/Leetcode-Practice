class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        remainder = time % (2 * n - 2)
        # print(f"cycle: {cycle} remainder: {remainder}")
        return remainder + 1 if remainder < n else 2 * n - remainder - 1