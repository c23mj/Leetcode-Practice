import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sort: n log n
        # return sorted(nums)[-k]

        # using a heap
        pq = []
        for num in nums:
            if len(pq) >= k:
                heapq.heappushpop(pq, num)
            else:
                heapq.heappush(pq, num)
        return pq[0]


        # quick select - TLE on non-random, long cases.
        
        # select a pivot scheme (Lomuto)
        # def partition():
        #     nonlocal l, r, nums, pivot_idx
        #     pivot = nums[pivot_idx]
        #     swap_idx = l
        #     nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
        #     for i in range(l, r):
        #         if nums[i] < pivot:
        #             nums[swap_idx], nums[i] = nums[i], nums[swap_idx]
        #             swap_idx += 1
        #     nums[swap_idx], nums[r] = nums[r], nums[swap_idx]
        #     return swap_idx

        # l, r = 0, len(nums)  - 1
        # while True:
        #     pivot_idx = random.randint(l, r)
        #     res_idx = partition()  
        #     if res_idx == len(nums) - k:
        #         return nums[res_idx]
        #     elif res_idx > len(nums) - k:
        #         r = res_idx - 1
        #     else:
        #         l = res_idx + 1

        
