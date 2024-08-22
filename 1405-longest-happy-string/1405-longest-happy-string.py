import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap, res = [], []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count < 0:
                heapq.heappush(heap, (count, char))
        while heap:
            bestCount, bestChar = heapq.heappop(heap)
            if len(res) < 2 or bestChar != res[-1] or bestChar != res[-2]:
                res.append(bestChar)
                bestCount += 1
                if bestCount < 0:
                    heapq.heappush(heap, (bestCount, bestChar))
            else:
                if not heap:
                    break
                nextCount, nextChar = heapq.heappop(heap)
                res.append(nextChar)
                nextCount += 1
                if nextCount < 0:
                    heapq.heappush(heap, (nextCount, nextChar))
                heapq.heappush(heap, (bestCount, bestChar))
        return ''.join(res)