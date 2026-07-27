"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def something(x):
            if not x:
                return 

            if x in visited:
                return visited[x]

            output = Node(x.val)
            visited[x] = output

            listii = []
            for n in x.neighbors:
                listii.append(something(n))

            output.neighbors = listii

            return output 

        return something(node)