# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def find_max(root):
            nonlocal res
            if not root:
                return 0
            elif not root.left and not root.right:
                res = max(res,root.val)
                return max(0,root.val)
            elif not root.right:
                left = root.val+find_max(root.left)
                res = max(res,root.val,left)
                return max(0,root.val,left)
            elif not root.left:
                right = root.val+find_max(root.right)
                res = max(res,root.val,right)
                return max(0,root.val,right)
            else:
                left = find_max(root.left)
                right = find_max(root.right)
                combine = root.val+left+right
                res = max(res,root.val,combine)
                return max(0,root.val,root.val+right,root.val+left)
        find_max(root)
        return res

            
