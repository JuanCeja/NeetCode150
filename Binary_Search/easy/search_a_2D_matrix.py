# 
# 
# 
# 
# 

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    left, right = 0, len(matrix)
    
    while left < right:
        mid = (right + left) // 2

        if target in matrix[mid]:
            return True
        elif target > matrix[mid][-1]:
            left = mid + 1
        else:
            right = mid

    return False

print(search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10)) # true
print(search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15)) # false