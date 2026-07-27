# 
# 
# 


def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    stack = []
    pairs = sorted(zip(position, speed), reverse=True)

    for pos, spd in pairs:
        time = (target - pos) / spd

        if not stack or time > stack[-1]:
            stack.append(time)

    return len(stack)


print(car_fleet(10, [1, 4], [3, 2])) # 1
print(car_fleet(10, [4, 1, 0, 7], [2, 2, 1, 1])) # 3