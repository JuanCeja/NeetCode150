# 
# 
# 
# 
# 

import math


def min_eating_speed(piles: list[int], h: int) -> int:
    l, r = 1, max(piles)
    res = float("inf")

    while l <= r:
        mid = (l + r) // 2

        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile / mid)

        if total_time > h:
            l = mid + 1
        else:
            res = min(res, mid)
            r = mid - 1
        
    return res

print(min_eating_speed([1,4,3,2], 9)) # 2
print(min_eating_speed([25,10,23,4], 4)) # 25