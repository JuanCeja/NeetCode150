# 
# 
# 
# 
# 
# 


def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2

        if nums[l] > nums[r]:
            l = mid + 1
        else:
            break

    res = float("inf")

    while l <= r:
        mid = (l + r) // 2

        

print(search([3,4,5,6,1,2], 1)) # 4
print(search([3,5,6,0,1,2], 4)) # -1