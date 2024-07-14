# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode()
        new_tmp = dummy
        tmp = head.next
        curr_sum = 0
        while tmp:
            if tmp.val == 0:
                new_tmp.next = ListNode(curr_sum)
                new_tmp = new_tmp.next
                curr_sum = 0
            curr_sum += tmp.val
            tmp = tmp.next
        return dummy.next
            
