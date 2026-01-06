# 
# 
# 


def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    fleets = 0
    stack = []
    
    # iterate position and speed
    for i in range(len(position)):
    
        # get length of time to target
        time_to_target = target / speed[i]
        
        # while current length of time < last in the stack 
        while stack and time_to_target < stack[-1]:
            # keep popping until stack is empty, add to fleet, then add current time to stack
            while stack:
                stack.pop()
            fleet += 1
        # add current length of time to stack
        stack.append(time_to_target)
    # return fleets
    return fleets


print(car_fleet(10, [1, 4], [3, 2])) # 1
print(car_fleet(10, [4, 1, 0, 7], [2, 2, 1, 1])) # 3