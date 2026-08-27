from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = Node()
        curr1, curr2 = l1, l2
        carry_over = 0

        while curr1 or curr2 or carry_over > 0:
            v1 = curr1.val if curr1.val else 0
            v2 = curr2.val if curr2.val else 0
            total = v1 + v2
            carry_over = total // 10
            new_node = ListNode(total % 10)
            dummy.next = new_node
            curr1 = curr1.next
            curr2 = curr2.next

        return dummy