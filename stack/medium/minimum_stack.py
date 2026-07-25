# 
# 
# 

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min:
            self.min.append(min(self.min[-1], val))
        else:
            self.min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin()) # return 0
minStack.pop()
print(minStack.top())    # return 2
print(minStack.getMin()) # return 1