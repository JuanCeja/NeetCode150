class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
    
    def getKthNode(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = k
        curr = head

        while curr and count > 0:
            curr = curr.next
            count -= 1

        return curr