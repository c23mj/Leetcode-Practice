# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        counts = dict()
        while head:
            if head.val in counts:
                counts[head.val] = -1
            else:
                counts[head.val] = 1
            head = head.next
            
        sortedUnique = sorted([key for key in counts if counts[key] == 1])
        dummy = ListNode()
        tmp = dummy
        for val in sortedUnique:
            tmp.next = ListNode(val)
            tmp = tmp.next
        return dummy.next
    