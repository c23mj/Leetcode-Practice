# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(0)
        num = 0
        temp = head
        while temp:
            num = num * 10 + temp.val
            temp = temp.next
        doubledStr = str(num * 2)
        if len(doubledStr) > len(str(num)):
            newHead = ListNode(next = head)
            head = newHead
        temp = head
        for i in range(len(doubledStr)):
            temp.val = (doubledStr[i])
            temp = temp.next
        return head
