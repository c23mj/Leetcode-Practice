import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = sorted(nums)[-k:]
        heapq.heapify(self.pq)
        
    def add(self, val: int) -> int:
        if len(self.pq) == self.k:
            heapq.heappushpop(self.pq, val)
        else:
            heapq.heappush(self.pq, val)
        
        return self.pq[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
    # param_1 = obj.add(val)