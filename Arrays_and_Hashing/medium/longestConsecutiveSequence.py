# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [2,20,4,10,3,4,5]
# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:
# Input: nums = [0,3,2,5,4,6,1,1]
# Output: 7

def longest_consecutive(nums: list[int]) -> int:
    nums_set = set(nums)
    max_count = 0

    for num in nums:
        if num - 1 in nums_set:
            continue

        count = 1

        while num + 1 in nums_set:
            num += 1
            count += 1

        max_count = max(count, max_count)

    return max_count


print(longest_consecutive([2,20,4,10,3,4,5])) # 4
print(longest_consecutive([0,3,2,5,4,6,1,1])) # 7