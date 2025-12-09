# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example 1:
# Input: height = [0,2,0,3,1,0,1,3,2,1]
# Output: 9

def trap(heights: list[int]) -> int:
    l_max, r_max = 0, 0
    left, right = 0, len(heights) - 1
    result = 0

    while left < right:
        if heights[left] < heights[right]:
            l_max = max(l_max, heights[left])
            result += l_max - heights[left]
            left += 1
        else:
            r_max = max(r_max, heights[right])
            result += r_max - heights[right]
            right -= 1

    return result

print(trap([0,2,0,3,1,0,1,3,2,1])) # 9