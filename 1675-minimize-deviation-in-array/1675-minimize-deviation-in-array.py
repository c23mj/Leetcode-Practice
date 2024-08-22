import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        maxHeap = []
        minVal, minDev = float('inf'), float('inf')
        for num in nums:
            if num % 2 == 0:
                num *= -1
            else:
                num *= -2
            heapq.heappush(maxHeap, num)
            minVal = min(minVal, -num)
        while maxHeap[0] % 2 == 0:
            nextMax = heapq.heappop(maxHeap)
            minDev = min(minDev, -(minVal + nextMax))
            minVal = min(minVal, -nextMax//2)
            heapq.heappush(maxHeap, nextMax // 2)
        minDev = min(minDev, -(minVal + maxHeap[0]))
        return minDev




        
   