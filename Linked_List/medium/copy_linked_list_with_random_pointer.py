# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        curr = head
        dummy = Node(0, head, 0)
        map = {}
        
        while curr:
            map[curr] = Node(curr.val, curr.next, curr.random)
            curr = curr.next
            
        curr = head
        
        while curr:
            dummy.val = map[curr].val
            dummy.next = map[curr].next
            dummy.random = map[curr].random
            curr = curr.next
        
        return dummy