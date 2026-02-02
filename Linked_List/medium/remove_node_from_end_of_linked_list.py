# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pointer = head
        
        for i in range(len(head)):
            pointer = pointer.next
            
        while pointer.next:
            dummy = dummy.next
            pointer = pointer.next
            
        removed_node = dummy.next
        removed_node.next = None
        dummy.next = dummy.next.next
        
        return head