class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        picked = sorted(happiness, reverse = True)[0:k]
        addend = sum(i - picked[i] for i in range(k) if i > picked[i])
        return sum(picked) - k * (k-1)//2 + addend