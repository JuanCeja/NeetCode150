# 
# 
# 


def daily_temperature(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    stack = []

    for idx, num in enumerate(temperatures):
            
            while stack and num > temperatures[stack[-1]]:
                res[stack[-1]] = idx - stack[-1]
                stack.pop()

            stack.append(idx)

    return res

print(daily_temperature([30,38,30,36,35,40,28])) # [1,4,1,2,1,0,0]
print(daily_temperature([22,21,20])) # [0,0,0]