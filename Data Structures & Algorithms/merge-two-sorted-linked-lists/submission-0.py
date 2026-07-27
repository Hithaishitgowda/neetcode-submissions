class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        current1 = list1
        current2 = list2

        dummy = ListNode()
        current = dummy

        while current1 and current2:
            if current1.val <= current2.val:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next

            current = current.next

        if current1:
            current.next = current1
        else:
            current.next = current2

        return dummy.next