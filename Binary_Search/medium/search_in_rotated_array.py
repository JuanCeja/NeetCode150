# 
# 
# 
# 
# 
# 


def search(nums: list[int], target: int) -> int:
    
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        mid_value = nums[mid]
        
        if mid_value == target:
            return mid

        if mid_value < target and nums[mid + 1] < mid_value:
            l = mid + 1
        else: 
            r = mid - 1

    return -1

print(search([3,4,5,6,1,2], 1)) # 4
print(search([3,5,6,0,1,2], 4)) # -1