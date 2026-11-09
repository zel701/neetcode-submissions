# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def same_tree(root,root2):
            if not root and not root2:
                return True
            elif not root or not root2 or root.val!=root2.val:
                return False
            return same_tree(root.left,root2.left) and same_tree(root.right,root2.right)
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if same_tree(node,subRoot):
                    return True
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
