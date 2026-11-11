# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode(None,None)
        res = ans

        while l1 and l2:
            current = (l1.val+l2.val+carry)%10
            carry = (l1.val+l2.val+carry)//10
            current_node = ListNode(current,None)
            res.next = current_node
            res = res.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            res.next = ListNode((l1.val+carry)%10,None)
            carry = (l1.val+carry)//10
            res = res.next
            l1 = l1.next
        while l2:
            res.next = ListNode((l2.val+carry)%10,None)
            carry = (l2.val+carry)//10
            res = res.next
            l2 = l2.next
        while carry:
            res.next = ListNode(carry,None)
            res = res.next
            carry = 0
        return ans.next

