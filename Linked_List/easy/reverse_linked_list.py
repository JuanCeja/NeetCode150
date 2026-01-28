# 
# 
# 
# 
# 
# 
# 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        forward = head.next
        head.next = None
        
        while forward:
            fast_forward = forward.next
            forward.next = prev
            prev = forward
            forward = fast_forward
            
        return head