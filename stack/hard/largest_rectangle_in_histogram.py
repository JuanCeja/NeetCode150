#
#
#
#
#

def largest_rectangle_area(heights: list[int]) -> int:
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights):
        start = i
        
        while stack and h < stack[-1][1]:
            idx, height = stack.pop()
            start = idx
            area = (i - idx) * height
            max_area = max(max_area, area)
            
        stack.append((start, h))
        
        
    for i, h in stack:
        area = (len(heights) - i) * h
        max_area = max(max_area, area)
        
    return max_area


print(largest_rectangle_area([7,1,7,2,2,4])) # 8
print(largest_rectangle_area([1,3,7])) # 7