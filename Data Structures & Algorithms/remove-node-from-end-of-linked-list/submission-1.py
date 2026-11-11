# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        start = head
        if head.next == None:
            return None
        while start:
            start = start.next
            count+=1
        print(count)
        dummy = ListNode(None,None)
        dummy.next = head
        index = count - n
        start = dummy
        while index>0:
            start = start.next
            index-=1
        start.next = start.next.next
        return dummy.next