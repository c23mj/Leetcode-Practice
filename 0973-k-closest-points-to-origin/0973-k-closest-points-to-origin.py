class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(k):
            point = points[i]
            heapq.heappush(heap, (-point[0] * point[0] - point[1] * point[1], point))
        for i in range(k, len(points)):
            point = points[i]
            heapq.heappushpop(heap, (-point[0] * point[0] - point[1] * point[1], point))
        return [tup[1] for tup in heap]