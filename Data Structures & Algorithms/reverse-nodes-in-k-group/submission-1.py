# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(root):
            pre = None
            cur = root
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        dummy = ListNode(None,None)
        current = head
        dummy.next = current 
        count = 0
    
        while current:
            count+=1
            current=current.next
        time = count//k
        idx = 0
        current = head
        current_count = 0
        current_head = dummy
        temp = None
        while time:
            while current_count<k-1 and current:
                current_count+=1
                current = current.next
            if current == None:
                break
            temp = current.next 
            current.next = None
            group_start = current_head.next
            node_reverse = reverse(group_start)
            current_head.next = node_reverse
            group_start.next = temp
            current = temp
            current_count = 0
            current_head = group_start
            time-=1
        return dummy.next
            