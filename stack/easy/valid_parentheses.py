# 
# 
# 

def is_valid(s: str) -> bool:

    stack = []

    close_to_open = {
        "}":"{",
        ")":"(",
        "]":"["
    }

    for r in range(len(s)):
        if s[r] in close_to_open:
            if stack and stack[-1] != close_to_open[s[r]]:
                return False
            else:
                stack.pop()
        else:
            stack.append(s[r])

    return len(stack) == 0


print(is_valid("[]")) # true
print(is_valid("([{}])")) # true
print(is_valid("[(])")) # false