# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example 1:
# Input: height = [0,2,0,3,1,0,1,3,2,1]
# Output: 9

def trap(heights: list[int]) -> int:
    l, r = 0, len(heights) - 1
    lmax, rmax = heights[l], heights[r]
    total_water = 0

    while l <= r:
        if lmax < rmax:
            lmax = max(heights[l], lmax)
            water = lmax - heights[l]
            total_water += water
            l += 1
        else:
            rmax = max(heights[r], rmax)
            water = rmax - heights[r]
            total_water += water
            r -= 1

    return total_water



print(trap([0,2,0,3,1,0,1,3,2,1])) # 9