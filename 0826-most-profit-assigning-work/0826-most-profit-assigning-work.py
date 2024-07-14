class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pairs = list(zip([-prof for prof in profit], difficulty))
        pairs.sort(key = lambda x: x[1])
        
        i, curr, maxProfit = 0, 0, 0
        worker.sort()

        heap = []

        while i < len(worker):
            while curr < len(pairs) and worker[i] >= pairs[curr][1]:
                heapq.heappush(heap, pairs[curr][0])
                curr += 1
            if heap:
                maxProfit += heap[0]
            i += 1

        return -maxProfit

        
