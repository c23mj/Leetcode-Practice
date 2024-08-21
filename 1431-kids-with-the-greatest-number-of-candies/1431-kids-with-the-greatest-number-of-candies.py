class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        out = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                out[i] = True
        return out