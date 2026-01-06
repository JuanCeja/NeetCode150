# 
# 
# 


def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    stack = []

    cars = sorted(zip(position, speed))
    print(cars)

    for pos, spd in reversed(cars):
        time = (target - pos) / spd

        stack.append(time)

        if len(stack) > 1 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


print(car_fleet(10, [1, 4], [3, 2])) # 1
print(car_fleet(10, [4, 1, 0, 7], [2, 2, 1, 1])) # 3