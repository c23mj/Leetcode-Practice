class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = list(zip([-profit for profit in profits], capital))
        pairs.sort(key = lambda x: x[1])
        curr = 0
        heap = []

        totalCapital = w
        # initial push
        while curr < len(pairs) and pairs[curr][1] <= totalCapital:
            heapq.heappush(heap, pairs[curr][0])
            curr += 1
            
        for i in range(k):
            if not heap:
                break
            neg_profit = heapq.heappop(heap)
            totalCapital += -neg_profit
            # keep pushing
            while curr < len(pairs) and pairs[curr][1] <= totalCapital:
                heapq.heappush(heap, pairs[curr][0])
                curr += 1

        return totalCapital