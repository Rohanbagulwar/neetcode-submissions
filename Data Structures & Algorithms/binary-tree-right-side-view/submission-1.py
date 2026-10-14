# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root):
        ls = []

        def dfs(level, root):
            if root is None:
                return

            if len(ls) == level:
                ls.append(root.val)

            dfs(level + 1, root.right)
            dfs(level + 1, root.left)

        dfs(0, root)
        return ls
        