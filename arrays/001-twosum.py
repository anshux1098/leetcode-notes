# Pattern: HashMap (complement lookup)
# Time: O(n) | Space: O(n)
# Approach: store complement in dict, check on each iteration

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i