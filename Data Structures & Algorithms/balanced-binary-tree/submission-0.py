# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        diff = 0 
        def depth(node):
            nonlocal diff
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            diff = max(diff, abs(left_depth - right_depth))

            return 1 + max(left_depth, right_depth)

        depth(root)
        if diff > 1:
            return False
           
        else: 
            return True
            