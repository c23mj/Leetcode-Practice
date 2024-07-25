class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        return list(sorted(counts.keys(), key=lambda x: counts[x], reverse=True))[:k]