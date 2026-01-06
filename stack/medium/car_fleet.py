# 
# 
# 


def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    stack = []

    sorted_fleets = sorted([p, s] for p, s in zip(position, speed))

    for i in range(len(sorted_fleets))[::-1]:
        time = (target - sorted_fleets[i][0]) / sorted_fleets[i][1]

        stack.append(time)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


print(car_fleet(10, [1, 4], [3, 2])) # 1
print(car_fleet(10, [4, 1, 0, 7], [2, 2, 1, 1])) # 3