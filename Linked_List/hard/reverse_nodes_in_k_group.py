class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow, fast, dummy = head, head, head
        slow_counter, fast_counter = 0, 0

        while slow and fast:
            slow = slow.next
            fast = fast.next.next
            slow_counter += 1
            fast_counter += 2

        if (fast_counter - slow_counter) >= k:
            end_of_first_half = slow
            beggining_of_second_half = slow.next
            end_of_second_half = fast

            self.reverseList(end_of_first_half)
            self.reverseList(end_of_second_half)

            beggining_of_second_half.next = end_of_first_half

        return dummy


        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev