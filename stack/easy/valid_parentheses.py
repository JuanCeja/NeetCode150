# 
# 
# 
# 
# 
# 
# 
# 

def is_valid(s: str) -> bool:
    # stack
    stack = []
    # iterate s
    for char in s:
        # if an opening bracket
        if char == "(" or char == "{" or char == "[":
            # push to stack
            stack.append(s)
            continue
        # if ) and stack -1 is ( pop
        if char == ")" and stack[-1] == "(":
            stack.pop()

        if char == "}" and stack[-1] == "{":
            stack.pop()

        if char == "]" and stack[-1] == "[":
            stack.pop()
        
    
    # return stack empty = true else false
    return True if len(stack) == 0 else False
    
    
    return True

print(is_valid("[]")) # true
print(is_valid("([{}])")) # true
print(is_valid("[(])")) # false
