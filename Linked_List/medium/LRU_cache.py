class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if self.dic[key]:
            return self.dic[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        while len(self.dic) >= self.capacity:
            self.remove()
            self.insert(Node(key, int))
    
    def insert(self, node):
        if len(self.dic) >= self.capacity:
            self.remove()
            
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next, self.right.prev = self.right, node
        
    def remove(self, node):
        curr = self.left.next
        next = curr.next
        self.left.next = next
        next.prev = self.left
        curr.next, curr.prev = None, None
        del self.dic[node]