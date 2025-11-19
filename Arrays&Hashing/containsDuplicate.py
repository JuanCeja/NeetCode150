# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false


def has_duplicate(nums: list[int]) -> bool:
    """Check if the list contains any duplicate values."""
    seen = set()

    for num in nums:
        if num in seen:
            return True
        
        seen.add(num)
    
    return False



print(has_duplicate([1, 2, 3, 3]))
print(has_duplicate([1, 2, 3, 4]))
