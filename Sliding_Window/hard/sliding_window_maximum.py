# 
# 
# 
# 
# 



from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    d = deque()
    res = []

    for r in range(len(nums)):
        while d and nums[r] > nums[d[-1]]:
            d.pop()
        d.append(r)

        if d and d[0] <= r - k:
            d.popleft()

        if r >= k - 1:
            res.append(nums[d[0]])

    return res

print(max_sliding_window([1,2,1,0,4,2,6], 3)) # [2,2,4,4,6]