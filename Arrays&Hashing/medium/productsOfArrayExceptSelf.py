# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in O(n)
# O(n) time without using the division operation?

# Example 1:               
#               [1,1,1,1]

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]

# Example 2:                 
# Input: nums = [-1,0,1,2,3]
#                          
# Output: [0,-6,0,0,0]

def product_except_self(nums: list[int]) -> list[int]:
    """Return product of all elements except self."""
    
    prefix = [1] * len(nums)

    for i in range (1, len(nums)):
        prefix[i] = nums[i - 1] * prefix[i - 1]


    postfix = [1] * len(nums)

    for i in range (len(nums) - 2, -1, -1):
        postfix[i] = nums[i + 1] * postfix[i + 1]
    result = [0] * len(nums)

    
    for i in range(len(result)):
        result[i] = prefix[i] * postfix[i]

    return result

print(product_except_self([1,2,4,6]))    # [48,24,12,8]
print(product_except_self([-1,0,1,2,3])) # [0,-6,0,0,0]
