"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new = {None:None}

        current = head

        while current:
            new[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            copy = new[current]
            copy.next = new[current.next]
            copy.random = new[current.random]

            current = current.next

        return new[head]