# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2

        dummy = ListNode(0)
        current = dummy 

        carry = 0

        while current1 or current2:
            
            value1 = current1.val if current1 else 0
            value2 = current2.val if current2 else 0

            value = value1 + value2 + carry
            digit = value % 10
            carry = value // 10 

            current.next = ListNode(digit)
            current = current.next

            if current1:
                current1 = current1.next
            if current2:
                current2 = current2.next

        if carry:
            current.next = ListNode(carry)

        return dummy.next