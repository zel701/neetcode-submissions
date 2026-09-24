# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root.val == p.val or root.val == q.val:
            return root
        def findNode(node,target):
            if node is None:
                return False
            stack = [node]
            while stack:
                newNode = stack.pop()
                if newNode.val == target:
                    return True
                if newNode.left:
                    stack.append(newNode.left)
                if newNode.right:
                    stack.append(newNode.right)
            return False
        if findNode(root.left,p.val) and findNode(root.right,q.val):
            return root
        elif findNode(root.left,q.val) and findNode(root.right,p.val):
            return root
        elif findNode(root.left,q.val) and findNode(root.left,p.val):
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)
                
        
    
        