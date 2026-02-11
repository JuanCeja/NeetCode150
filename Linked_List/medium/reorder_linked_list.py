
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        slow.next = None
        second_half = self.reverse_list(second)
        self.merge_lists(head, second_half)

        return None
        
        
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev
    

    def merge_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> None:
        if not list1 or not list2:
            return list1 or list2
        
        dummy = ListNode()
        curr = dummy
        count = 0

        while list1 and list2:
            if count % 2 == 0:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
            count += 1
            
        if list1:
            curr.next = list1
        
        if list2:
            curr.next = list2

        return
