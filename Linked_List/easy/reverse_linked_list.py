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
        if head == None: return head
        
        forward = head.next
        prev = head
        prev.next = None
        
        while forward:
            fast_forward = forward.next
            forward.next = prev
            prev = forward
            forward = fast_forward
            head = prev

        return head