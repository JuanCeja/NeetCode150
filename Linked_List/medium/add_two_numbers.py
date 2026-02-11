from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1, curr_2 = l1, l2
        carry_over = 0
        dummy = ListNode(0)
        current = dummy
        
        while curr_1 or curr_2 or carry_over:
            sum = (curr_1.val if curr_1 else 0) + (curr_2.val if curr_2 else 0)
            
            total = sum + carry_over
            carry = total // 10
            digit = total % 10
            
            current.next = ListNode(digit)
            current = current.next
            curr_1 = curr_1.next
            curr_2 = curr_2.next
        
        while curr_1.next is not None:
            current.val = curr_1.val
            current.next = ListNode()
            curr_1 = curr_1.next

        while curr_2.next is not None:
            current.val = curr_2.val
            current.next = ListNode()
            curr_2 = curr_2.next
            
        return dummy