# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example 1:
# Input: height = [0,2,0,3,1,0,1,3,2,1]
# Output: 9

def trap(heights: list[int]) -> int:
    # create our left and max
    # create l and r
    # result

    # while l < r

        # get minimum of both

        # calculate our possible water for that spot
        
        # current water = minimum - level

        # if cw > 0:

            # add to cw to result

        # else:
            # if l < r move left
                
            # else move right

print(trap([0,2,0,3,1,0,1,3,2,1])) # 9