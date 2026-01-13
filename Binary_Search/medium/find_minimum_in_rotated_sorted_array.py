# 
# 
# 
# 
# 

def find_min(nums: list[int]) -> int:

    l, r = 0, len(nums) - 1
    min_num = float("inf")
    
    if nums[l] < nums[r] or len(nums) < 2:
        return nums[0]
    
    while l <= r:
        mid = (l + r) // 2
        min_num = min(min_num, nums[mid])
        
        if nums[mid] <= nums[r]:
            r = mid - 1
        else:
            l = mid + 1
            
    return min_num


print(find_min([3,4,5,6,1,2])) # 1
print(find_min([4,5,0,1,2,3])) # 0
# [9 1 2 3 4 5]