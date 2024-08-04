# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        curr = head
        while curr:
            sz += 1
            curr = curr.next    

        dummy = ListNode(val=0, next=head)
        deleteIdx = sz - n
        curr = dummy
        for i in range(deleteIdx):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next