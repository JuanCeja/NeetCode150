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


        if target == nums[mid]:
            return mid
        elif nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    else:
        return -1


print(search([3,4,5,6,1,2], 1)) # 4
print(search([3,5,6,0,1,2], 4)) # -1