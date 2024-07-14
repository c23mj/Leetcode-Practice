import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        pq = []
        score = 0
        for i in range(len(nums)):
            heapq.heappush(pq, (nums[i], i))
        while pq:
            top = heapq.heappop(pq)
            if top[1] not in marked:
                # print("mark " + str(top))
                score += top[0]
                marked.update([top[1] - 1, top[1], top[1] + 1])
            # print("marked: " + str(marked))
        return score