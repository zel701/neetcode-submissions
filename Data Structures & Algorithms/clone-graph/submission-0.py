"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from queue import PriorityQueue
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        startVal = node.val
        queue = PriorityQueue()
        queue.put((node.val,node))
        res = []
        adjalist = deque()
        visited = {node}
        while not queue.empty():
            node = queue.get()
            current =[]
            if node:
                for i in node[1].neighbors:
                    if i not in visited:
                        queue.put((i.val,i))
                        visited.add(i)
                    current.append(i.val)
                adjalist.append([node[1].val,current])
        
        newNodes = {}
        for val,neighbors in adjalist:
            newNodes[val] = Node(val)
        for val,neighbors in adjalist:
            newNeighbors = []
            for neighborVal in neighbors:
                newNeighbors.append(newNodes[neighborVal])
            newNodes[val].neighbors = newNeighbors
        return newNodes[startVal]