# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        copies = {None: None}
        curr = head

        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = copies[curr]
            copy.next = copies[curr.next.val]
            copy.random = copies[curr.random]

        return head