# 
# 
# 
# 
# 

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    top, bottom = 0, len(matrix) - 1

    while top <= bottom:
        mid_row = (top + bottom) // 2

        if target > matrix[mid_row][-1]:
            top = mid_row + 1
        elif target < matrix[mid_row][0]:
            bottom = mid_row - 1
        else:
            break
    else:
        return False

    row = matrix[mid_row]
    left, right = 0, len(row) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == row[mid]:
            return True
        elif target > row[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10)) # true
print(search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15)) # false