# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        count = 0
        while curr:
            count += 1
            stack.append(curr)
            curr = curr.next
        stack = stack[(count + 1)//2:]
        curr = head
        while stack:
            nxt = curr.next
            curr.next = stack.pop()
            # print(f"setting {curr.val} next -> {curr.next.val}")
            curr.next.next = nxt
            # print(f"setting {curr.next.val} next -> {nxt.val}")
            curr = nxt
            # print(f"setting curr to {nxt.val}")

        curr.next = None
        
        """
        Do not return anything, modify head in-place instead.
        """
        