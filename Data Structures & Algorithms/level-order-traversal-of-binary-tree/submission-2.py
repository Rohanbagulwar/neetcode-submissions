# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result=[]
        q=queue.Queue()
        q.put(root)

        while not q.empty():
            level_size=q.qsize()
            level_nodes=[]

            for _ in range(level_size):
                node=q.get()
                level_nodes.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

            result.append(level_nodes)
        return result