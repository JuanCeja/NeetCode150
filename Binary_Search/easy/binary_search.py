# 
# 
# 
# 
# 


def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    
    while left < right:
        mid = (right + left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1
            
    return -1

print(binary_search([-1,0,2,4,6,8], 4)) # 3
print(binary_search([-1,0,2,4,6,8], 3)) # -1