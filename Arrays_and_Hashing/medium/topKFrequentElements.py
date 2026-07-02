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
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1
            
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in counts.items():
        buckets[freq].append(num)

    result = []

    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)

            if len(result) == k:
                return result


print(top_k_frequent([1,2,2,3,3,3], 2))
print(top_k_frequent([7, 7], 1))