# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        output = []

        while queue:
            level = []

            for _ in range(len(queue)):
                res = queue.pop(0)
                level.append(res.val)
            
                if res.left:
                    queue.append(res.left)
            
                if res.right:
                    queue.append(res.right)

            output.append(level)
        return output



