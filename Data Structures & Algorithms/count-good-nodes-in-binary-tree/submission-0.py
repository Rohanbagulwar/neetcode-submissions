# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper_function(root, max_value):
            if root is None:
                return 0

            ans = 0

            if root.val >= max_value:
                ans = 1

            max_value = max(max_value, root.val)

            lans = helper_function(root.left, max_value)
            rans = helper_function(root.right, max_value)

            return ans + lans + rans

        return helper_function(root, root.val)