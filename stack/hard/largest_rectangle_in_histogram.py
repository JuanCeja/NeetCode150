#
#
#
#
#

def largest_rectangle_area(heights: list[int]) -> int:
    max_area = 0
    stack = []

    for idx, height in enumerate(heights):
        start = idx
        while stack and stack[-1][1] > height:
            popped_idx, popped_height = stack.pop()
            max_area = max(max_area, popped_height * (idx - popped_idx))
            start = popped_idx
        stack.append((start, height))

    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))

    return max_area


print(largest_rectangle_area([7,1,7,2,2,4])) # 8
print(largest_rectangle_area([1,3,7])) # 7