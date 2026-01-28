# 
# 
# 
# 
# 
# 
# 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow
        
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = ListNode()
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev.next
    
    # im working on getting my reverse linked list to work