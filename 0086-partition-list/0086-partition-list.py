# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        lower = ListNode()
        start = lower # start of list
        higher = ListNode()
        mid = higher # pivot
        while(head):
            if head.val < x:
                # print("added to lower: " + str(head.val))
                lower.next = head
                lower = lower.next
            else:
                # print("added to higher: " + str(head.val))
                higher.next = head
                higher = higher.next
            head = head.next
        # print(start)
        # print(mid)
        lower.next = mid.next
        higher.next = None
        return start.next
                

        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        