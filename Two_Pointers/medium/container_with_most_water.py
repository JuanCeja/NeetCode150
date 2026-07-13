# You are given an integer array heights where heights[i] represents the height of the 
# i-th bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:
# Input: height = [1,7,2,5,4,7,3,6]
# Output: 36

# Example 2:
# Input: height = [2,2,2]
# Output: 4

def max_area(heights: list[int]) -> int:
    max_area = 0
    l, r = 0, len(heights) - 1

    while l < r:
        height = min(heights[l], heights[r])
        width = r - l
        area = height * width

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

        max_area = max(area, max_area)

    return max_area

print(max_area([1,7,2,5,4,7,3,6])) # 36
print(max_area([2,2,2])) # 4