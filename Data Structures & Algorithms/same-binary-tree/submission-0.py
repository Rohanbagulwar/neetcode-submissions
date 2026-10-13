# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        
        def serialize(root):
            arr = []
            queue = deque([root])
            
            while queue:
                node = queue.popleft()
                
                if node:
                    arr.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    arr.append(None)
            
            return arr
        
        return serialize(p) == serialize(q)




        