# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return [-1, -1]
        left = head
        mid = head.next
        if not mid.next:
            return[-1, -1]
        right = mid.next
        idx, crits = 2, []
        while right:
            if (mid.val > left.val and mid.val > right.val) or \
               (mid.val < left.val and mid.val < right.val):
               crits.append(idx)
            left = mid
            mid = right
            right = right.next
            idx += 1

        if len(crits) < 2:
            return [-1, -1]
        
        min_dist = float("inf")
        for i in range(1, len(crits)):
            min_dist = min(min_dist, crits[i] - crits[i - 1])
        return [min_dist, crits[-1] - crits[0]]