from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0

        while nums[fast]:
            fast = nums[nums[fast]]
            slow = nums[slow + 1]


        if slow == fast:
            return slow


# nums = [1,2,3,2,2]