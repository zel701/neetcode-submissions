# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []
        current = []
        current_res = []
        if not root:
            return []
        while queue:
            node = queue.popleft()
            current_res.append(node.val)
            if node.left:
                current.append(node.left)
            if node.right:
                current.append(node.right)
            if not queue:
                queue.extend(current)
                res.append(current_res[-1])
                current = []
                current_res = []    
        return res
