# 
# 
# 

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        lowest_num = float("inf")
        
        for num in self.stack:
            lowest_num = min(lowest_num, num)
            
        return lowest_num

minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin()) # return 0
minStack.pop()
print(minStack.top())    # return 2
print(minStack.getMin()) # return 1