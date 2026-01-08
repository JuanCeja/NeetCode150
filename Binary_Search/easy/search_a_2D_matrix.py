# 
# 
# 
# 
# 

search_matrix(matrix: list[list[int]], target: int) -> bool:
    # use binary search in the outer arr

        # check if target is in between first and last num of our mid array

            # if so, use binary search in that array

                # if result is not found return false

        # if target > then last value in mid array

            # left = mid + 1

        # else 

            # right = mid



print(search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10)) # true
print(search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15)) # false