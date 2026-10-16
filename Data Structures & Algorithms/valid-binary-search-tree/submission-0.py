# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def nested_fun(root, value, flag, low, high):
            if root is None:
                return True

            if root.val <= low or root.val >= high:
                return False

            rside = nested_fun(root.right, root.val, True, root.val, high)
            lside = nested_fun(root.left, root.val, False, low, root.val)

            return rside and lside

        return nested_fun(root, 0, True, float('-inf'), float('inf'))

        