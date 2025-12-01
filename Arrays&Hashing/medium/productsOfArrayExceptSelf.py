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
    
    n = len(nums)

    prefix = [1] * n
    for i in range(1, n):
        prefix[i]  = prefix[i - 1] * nums[i - 1]

    postfix = [1] * n
    for i in range(n - 2, -1, -1):
        postfix[i] = postfix[i + 1] * nums[i + 1]

    return [postfix[i] * prefix[i] for i in range(n)]
            
print(product_except_self([1,2,4,6]))    # [48,24,12,8]
print(product_except_self([-1,0,1,2,3])) # [0,-6,0,0,0]
