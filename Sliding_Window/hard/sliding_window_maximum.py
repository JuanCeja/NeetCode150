# 
# 
# 
# 
# 



def max_sliding_window(nums: list[int], k: int) -> list[int]:
    
    res = []
    
    for index, value in enumerate(nums[:len(nums) - k + 1]):
        window = nums[index: index + k]
        max_value = max(window)
        res.append(max_value)
        
    return res

print(max_sliding_window([1,2,1,0,4,2,6], 3)) # [2,2,4,4,6]