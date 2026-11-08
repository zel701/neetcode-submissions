class Node:
    def __init__(self,key = None,value=None,pre=None,next_node=None):
        self.pre = pre
        self.value = value 
        self.key = key
        self.next_node = next_node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list = None
        self.cache = {}
        self.original = Node(None,None,None,None)
    def get(self, key: int) -> int:

        if self.cache.get(key):
            currentNode = self.cache[key]
            if currentNode == self.linked_list:
                return currentNode.value
            if currentNode.next_node:
                currentNode.next_node.pre = currentNode.pre
            currentNode.pre.next_node = currentNode.next_node
            if self.linked_list:
                self.linked_list.next_node = currentNode
                currentNode.pre=self.linked_list
                currentNode.next_node = None
                self.linked_list = currentNode
            else:
                currentNode.pre=self.original
                currentNode.next_node = None
                self.linked_list = currentNode
            return currentNode.value
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if self.linked_list:
            if not self.cache.get(key):
                newNode = Node(key,value,self.linked_list,None)
                self.linked_list.next_node = newNode
                self.linked_list = self.linked_list.next_node
                self.cache[key] = newNode
                self.capacity-=1
            else:
                
                self.cache[key].value = value
                currentNode = self.cache[key]
                if currentNode != self.linked_list:

                    if currentNode.next_node:
                        currentNode.next_node.pre = currentNode.pre
                    currentNode.pre.next_node = currentNode.next_node
                    if self.linked_list:
                        currentNode.pre=self.linked_list
                        currentNode.next_node = None
                        self.linked_list.next_node = currentNode
                        self.linked_list = currentNode
                    else:
                        currentNode.pre=self.original
                        currentNode.next_node = None
                        self.original.next_node = currentNode
                        self.linked_list = currentNode
        else:
            newNode = Node(key,value,self.original,self.original.next_node)
            self.linked_list = newNode
            self.original.next_node = self.linked_list
            self.cache[key] = newNode
            self.capacity-=1
        if self.capacity<0:
            removed = self.original.next_node
            self.original.next_node = self.original.next_node.next_node
            self.original.next_node.pre = self.original
            self.cache.pop(removed.key)
            self.capacity +=1
