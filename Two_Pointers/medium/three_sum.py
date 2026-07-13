# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

def threeSum(nums: list[int]) -> list[list[int]]:
    sorted_nums = sorted(nums)
    res = []

    for idx, num in enumerate(sorted_nums):

        left, right = idx + 1, len(sorted_nums) - 1

        if idx > 0 and num == sorted_nums[idx - 1]:
            continue

        while left < right:
            total = num + sorted_nums[left] + sorted_nums[right]

            if total == 0:
                res.append([num, sorted_nums[left], sorted_nums[right]])
                left += 1
                right -= 1

                while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                    left += 1
                while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                    right -= 1
            elif total > 0:
                right -= 1
            else:
                left += 1

    return res


print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(threeSum([0,1,1])) # []
print(threeSum([0,0,0])) # [[0,0,0]]