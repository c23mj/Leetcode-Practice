# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        h1, h2 = list1, list2
        while h1 and h2:
            if h1.val < h2.val:
                curr.next = h1
                curr = curr.next
                h1 = h1.next
            else:
                curr.next = h2
                curr = curr.next
                h2 = h2.next
        while h1:
            curr.next = h1
            curr = curr.next
            h1 = h1.next
        while h2:
            curr.next = h2
            curr = curr.next
            h2 = h2.next
        return dummy.next
            