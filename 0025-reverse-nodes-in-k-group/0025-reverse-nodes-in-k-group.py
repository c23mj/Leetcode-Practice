# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # first pass to get size
        ptr = head
        n = 0
        while(ptr):
            ptr = ptr.next
            n += 1

        if k == 1 or k > n: return head
        prev = None
        ptr = head
        curr = ptr
        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
    
        ptr.next = curr
        new_head = prev
        
        for i in range((n - k)//(k)):
            left = ptr
            ptr = curr
            prev = None
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            ptr.next = curr
            left.next = prev


        return new_head