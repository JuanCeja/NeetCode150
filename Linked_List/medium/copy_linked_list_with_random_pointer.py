# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        oldToCopy = {None: None}
        cur = head
        
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next
            
        cur = head
        
        while cur:
            new_node = oldToCopy[cur]
            new_node.next = oldToCopy[cur.next]
            new_node.random = oldToCopy[cur.random]
            cur = cur.next
            
        return oldToCopy[head]