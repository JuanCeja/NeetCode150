# 
# 
# 
# 
# 

def find_min(nums: list[int]) -> int:
    res = float("inf")
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        res = min(res, nums[mid])

        if nums[mid] < nums[r]:
            r = mid - 1
        else:
            l = mid + 1

    return res


print(find_min([3,4,5,6,1,2])) # 1
print(find_min([4,5,0,1,2,3])) # 0