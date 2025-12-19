# 
# 
# 
# 
# 

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    output = []
    q = deque()
    l = r = 0
    
    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)
        
        if l > q[0]:
            q.popleft()
            
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    
    return output


print(max_sliding_window([1,2,1,0,4,2,6], 3)) # [2,2,4,4,6]