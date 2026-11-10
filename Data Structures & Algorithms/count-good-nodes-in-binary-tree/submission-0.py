# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root,max_node):
            nonlocal count
            if not root:
                return 
            if root.val >= max_node:
                count+=1
            if root.right:
                dfs(root.right,max(max_node,root.val))
            if root.left:
                dfs(root.left,max(max_node,root.val))
        dfs(root,-101)
        return count