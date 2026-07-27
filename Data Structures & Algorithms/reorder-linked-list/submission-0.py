# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current1 = head 
        current2 = head

        stack = []

        while current1:
            stack.append(current1)
            current1 = current1.next

        for _ in range(len(stack)//2):
            next_node = current2.next

            current2.next = stack.pop()
            current2 = current2.next

            current2.next = next_node
            current2 = next_node

        current2.next = None 
        