import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        tmp = head
        heap = []
        i = 0
        for lst in lists:
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))
                i += 1
        while heap:
            _, __, nextNode = heapq.heappop(heap)
            if nextNode.next:
                heapq.heappush(heap, (nextNode.next.val, i, nextNode.next))
                i += 1
            tmp.next = nextNode
            tmp = tmp.next
        return head.next