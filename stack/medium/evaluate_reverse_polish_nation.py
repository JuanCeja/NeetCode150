# 
# 
# 

def evaluate_reverse_polish_notation(tokens: list[str]) -> int:
    stack = []
    
    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            right = stack.pop()
            left = stack.pop()
            stack.append(left - right)
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            right = stack.pop()
            left = stack.pop()
            stack.append(int(left / right))
        else:
            stack.append(int(token))
    
    return stack[0]

print(evaluate_reverse_polish_notation(["1","2","+","3","*","4","-"])) # 5
print(evaluate_reverse_polish_notation(["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"])) #22