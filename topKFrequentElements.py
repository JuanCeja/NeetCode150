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

    for num in nums:
        frequency_counter[num] = frequency_counter.get(num, 0) + 1

    bucket = [[] for _ in range(len(nums) +1 )]
    
    for num, freq in frequency_counter.items():
        bucket[freq].append(num)
    
    result = []
    
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result
            


print(top_k_frequent([1,2,2,3,3,3], 2))
print(top_k_frequent([7, 7], 1))