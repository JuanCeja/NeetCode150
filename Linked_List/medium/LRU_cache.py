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
        if key in self.dic:
            self.move_to_recent(self.dic[key])
            return self.dic[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].value = value
            self.move_to_recent(self.dic[key])
        
        else:
            node = Node(key, value)
            while len(self.dic) >= self.capacity:
                self.remove()
        
            self.insert(node)
    
    def insert(self, node: Node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next, self.right.prev = self.right, node
        self.dic[node.key] = node
        
    def remove(self, node: Node):
        curr = self.left.next
        next = curr.next
        self.left.next = next
        next.prev = self.left
        curr.next, curr.prev = None, None
        del self.dic[node]
        
    def move_to_recent(self, node: Node):
        prev = node.prev
        next = node.next
        last_node = self.right
        
        prev.next, next.prev = next, prev
        last_node.next, node.prev = node, last_node
        node.next, self.right.prev = self.right, node