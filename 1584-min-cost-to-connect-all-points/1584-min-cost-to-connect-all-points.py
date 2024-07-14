class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        curr, dist = tuple(points[0]), -1
        pointSet = set([tuple(point) for point in points])
        pointSet.discard(curr)
        totalCost = 0
        distances = []
        for i in range(len(points) - 1):
            # print(pointSet)
            for point in pointSet:
                heapq.heappush(distances, (abs(point[0] - curr[0]) + abs(point[1] - curr[1]), point))
            while curr not in pointSet:
                dist, curr = heapq.heappop(distances)
            # print(f"best: {curr}, dist: {dist}")
            totalCost += dist
            pointSet.discard(curr)
        return totalCost


