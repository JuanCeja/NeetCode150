# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    frequency_counter = {}
    frequent_elements = []

    for num in nums:
        if num in frequency_counter:
            frequency_counter[num] += 1
        else: frequency_counter[num] = 1

    sorted_items = sorted(frequency_counter.items(), key = lambda x: x[1])

    beggining = len(sorted_items) - k
    for i in sorted_items[beggining:len(sorted_items)]:
        frequent_elements.append(i[0])

    return frequent_elements

print(top_k_frequent([1,2,2,3,3,3], 2))
print(top_k_frequent([7, 7], 1))