from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1, curr_2 = l1, l2
        carry_over = False
        product = ListNode()
        
        while (curr_1 is not None or curr_2 is not None) and (curr_1.next and curr_2.next):
            sum = curr_1.val + curr_2.val
            
            if carry_over == True:
                sum += 1
                
            if sum > 10:
                sum = sum % 10
                carry_over = True
            
            product.val = sum
            carry_over = False
            product.next = ListNode
            curr_1 = curr_1.next
            curr_2 = curr_2.next
        
        while curr_1.next is not None:
            product.val = curr_1.val
            product.next = ListNode()
            curr_1 = curr_1.next

        while curr_2.next is not None:
            product.val = curr_2.val
            product.next = ListNode()
            curr_2 = curr_2.next
            
        return product