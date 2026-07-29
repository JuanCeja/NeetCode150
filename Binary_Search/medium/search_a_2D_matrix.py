# 
# 
# 
# 
# 

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    out_l, out_r = 0, len(matrix) - 1

    while out_l <= out_r:
        outter_mid = (out_l + out_r) // 2

        if target <= matrix[outter_mid][-1] and target >= matrix[outter_mid][0]:
            l, r = 0, len(matrix[outter_mid]) - 1

            while l <= r:
                inner_mid = (l + r) // 2
                if target == matrix[outter_mid][inner_mid]:
                    return True
                elif target > matrix[outter_mid][inner_mid]:
                    l = inner_mid + 1
                else:
                    r = inner_mid - 1
        elif target > matrix[outter_mid][-1]:
            out_l = outter_mid + 1
        else:
            out_r = outter_mid - 1

    return False


print(search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10)) # true
print(search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15)) # false