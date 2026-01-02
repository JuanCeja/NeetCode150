# 
# 
# 

def evaluate_reverse_polish_nation(tokens: list[str]) -> int:

    stack = []
    operators = {"+", "-", "*", "/"}

    for token in tokens:

        if token in operators:
            num_1 = stack.pop()
            num_2 = stack.pop()
                
            if token == "+":
                stack.append(num_1 + num_2)
            if token == "-":
                stack.append(num_2 - num_1)
            if token == "*":
                stack.append(num_1 * num_2)
            if token == "/":
                stack.append(int(num_2 / num_1))
        else:
            stack.append(int(token))
            
    return stack[0]

# print(evaluate_reverse_polish_nation(["1","2","+","3","*","4","-"])) # 5
print(evaluate_reverse_polish_nation(["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"])) #22