# 
# 
# 

def evaluate_reverse_polish_notation(tokens: list[str]) -> int:
    stack = []

    for num in tokens:
        if num in "+-*/":
            num_1 = stack.pop()
            num_2 = stack.pop()
            if num == "+":
                stack.append(num_1 + num_2)
            if num == "-":
                stack.append(num_2 - num_1)
            if num == "*":
                stack.append(num_1 * num_2)
            if num == "/":
                stack.append(int(num_2 / num_1))
        else:
            stack.append(int(num))

    return stack.pop()


print(evaluate_reverse_polish_notation(["1","2","+","3","*","4","-"])) # 5
print(evaluate_reverse_polish_notation(["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"])) #22