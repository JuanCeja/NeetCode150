# 
# 
# 
# 
# 

import math


def min_eating_speed(piles: list[int], h: int) -> int:
    
    left, right = 1, max(piles)
    
    while left < right:
        mid = (right + left) // 2
        sum_of_hours = 0
        
        for i in piles:
            sum_of_hours += math.ceil(i / mid)

        if sum_of_hours <= h:
            right = mid
        else:
            left = mid + 1
            
    return left

print(min_eating_speed([1,4,3,2], 9)) # 2
print(min_eating_speed([25,10,23,4], 4)) # 25