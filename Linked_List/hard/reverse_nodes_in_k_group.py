class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        while curr:
            if self.getKthNode(curr, k):
                beginning_of_group = curr.next
                end_of_group = curr
                self.reverseList(curr)
                beginning_of_group.next = end_of_group
            
        return curr


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