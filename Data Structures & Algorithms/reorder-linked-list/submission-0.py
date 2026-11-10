# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head):
            pre = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        list2 = slow.next
        list1 = head
        slow.next = None
        list2 = reverse(list2)
        dummy = ListNode(None,None)
        current = dummy
        while list1:
            if list1:
                current.next = list1
                list1=list1.next
                current = current.next
            if list2:
                current.next = list2
                list2=list2.next
                current = current.next