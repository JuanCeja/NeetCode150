# 
# 
# 

class MinStack:

    def __init__(self):

    def push(self, val: int) -> None:

    def pop(self) -> None:

    def top(self) -> int:

    def getMin(self) -> int:

minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin()) # return 0
minStack.pop()
print(minStack.top())    # return 2
print(minStack.getMin()) # return 1