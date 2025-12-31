# 
# 
# 

def is_valid(s: str) -> bool:
    stack = []
    close_to_open = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    
    for char in s:
        if char in close_to_open:
            if not stack or close_to_open[char] != stack[-1]:
                return False
            stack.pop()
        else:
            stack.append(char)
        
    return len(stack) == 0


print(is_valid("[]")) # true
print(is_valid("([{}])")) # true
print(is_valid("[(])")) # false