# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow_index, fast_index = 0, 0
        
        slow, fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            slow_index += 1
            fast_index += 2
            
        
        index_to_be_removed = (fast_index - n) - 1
        
        while slow_index != index_to_be_removed and slow:
            slow = slow.next
            slow_index += 1

        removed_node = slow.next
        slow.next = slow.next.next
        removed_node.next = None
        
        return head
