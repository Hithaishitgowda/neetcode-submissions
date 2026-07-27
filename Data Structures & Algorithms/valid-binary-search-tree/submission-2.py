# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def valid(lower_bound, node, upper_bound ):
            if not node:
                return True
            return(
                lower_bound < node.val < upper_bound
                and
                valid(lower_bound, node.left, node.val)
                and 
                valid(node.val, node.right, upper_bound)
            )


        return valid(float('-inf'), root, float('+inf'))
