# 
# 
# 
# 
# 

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    left, right = 0, len(matrix)
    
    while left < right:
        mid = (right + left) // 2

        if matrix[mid][0] <= target <= matrix[mid][-1]:
            row = matrix[mid]
            
            inner_left, inner_right = 0, len(row)

            while inner_left < inner_right:
                inner_mid = (inner_right + inner_left) // 2

                if row[inner_mid] == target: 
                    return True
                elif target > row[inner_mid]:
                    inner_left = inner_mid + 1
                else:
                    inner_right = inner_mid
                    
            return False

        elif target > matrix[mid][-1]:
            left = mid + 1
        else:
            right = mid

    return False

print(search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10)) # true
print(search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15)) # false