# 
# 
# 


def daily_temperature(temperatures: list[int]) -> list[int]:
    result = [0] * len(temperatures)
    stack = []
    
    for i in range(len(temperatures)):
        
        while stack and temperatures[i] > temperatures[stack[-1]]:
            result[stack[-1]] = i - stack[-1]
            stack.pop()
            
        stack.append(i)
        
    return result

print(daily_temperature([30,38,30,36,35,40,28])) # [1,4,1,2,1,0,0]
print(daily_temperature([22,21,20])) # [0,0,0]