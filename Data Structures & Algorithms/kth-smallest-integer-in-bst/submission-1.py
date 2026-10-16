# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        counter = 0

        def traverse(root):
            nonlocal counter

            if root is None:
                return None

            left = traverse(root.left)
            if left is not None:
                return left

            counter += 1

            if counter == k:
                return root.val

            right = traverse(root.right)
            return right

        return traverse(root)

        