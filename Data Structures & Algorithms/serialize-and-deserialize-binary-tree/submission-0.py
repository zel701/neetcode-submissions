# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue = deque([root])
        res = ""
        res = res + str(root.val)+"*"
        current = []
        while queue:
            node = queue.popleft()
            if node.left:
                res = res + str(node.left.val)+"*"
            else:
                res = res + "N"+"*"
            current.append(node.left)
            if node.right:
                res = res + str(node.right.val)+"*"
            else:
                res = res + "N"+"*"
            current.append(node.right)
            if not queue:
                for i in current:
                    if i is not None:
                        queue.append(i)
                current = []
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        listData = data.split("*")
        listData.pop()
        listData = deque(listData)
        val = listData.popleft()
        root = TreeNode(val)
        level = deque()
        levelVal = deque()
        levelAmount = 2
        pre = deque([root])
        while listData:
            i = 0
            print(levelAmount)
            while i<levelAmount:
                node_val = listData.popleft()
                if node_val!="N":
                    new_node = TreeNode(node_val)
                    level.append(new_node)
                else:
                    level.append(None)
                i+=1
            i=0
            new_level = []
            levelAmount = 0
            for j in level:
                if j is not None:
                    levelAmount+=2
                    new_level.append(j)
            for k in pre:
                current = level.popleft()
                k.left = current
                current = level.popleft()
                k.right = current
            pre = new_level
            new_level = []
        return root
