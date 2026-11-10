# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        res = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            node = stack.pop()
            res.append(node.val)
            current = node.right
        return res[k-1]