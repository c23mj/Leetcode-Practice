class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-weight for weight in stones]
        heapq.heapify(pq)
        while len(pq) > 1:
            y, x = heapq.heappop(pq), heapq.heappop(pq)
            if y < x:
                heapq.heappush(pq, y - x)
        return -pq[0] if pq else 0
            
            
            