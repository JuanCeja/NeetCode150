# 
# 
# 

def is_valid(s: str) -> bool:
    stack = []

    close_to_open = {
        "}":"{",
        "]":"[",
        ")":"("
    }

    for char in s:
        if char in close_to_open:
            if stack and close_to_open[char] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return len(stack) == 0


print(is_valid("[]")) # true
print(is_valid("([{}])")) # true
print(is_valid("[(])")) # false