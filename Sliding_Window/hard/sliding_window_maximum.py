# 
# 
# 
# 
# 



from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    res = []
    dq = deque()
    
    for i in range(len(nums)):
        
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
            
        dq.append(i)
        
        if i - k + 1 > k:
            res.append(nums[dq[0]])
            
    return res

print(max_sliding_window([1,2,1,0,4,2,6], 3)) # [2,2,4,4,6]