# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(None,None)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i,lists[i]))
        current = dummy
        while heap:
            current_node = heapq.heappop(heap)
            current.next = current_node[2]
            current = current.next
            if lists[current_node[1]].next:
                lists[current_node[1]] = lists[current_node[1]].next
                heapq.heappush(heap,(lists[current_node[1]].val,current_node[1],lists[current_node[1]]))
        return dummy.next
            