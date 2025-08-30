# Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# NeetCode 150 – Two Pointers
# Difficulty: Medium
# Time: O(n), Space: O(1)

from typing import List, Tuple

class Solution:
    def twoSum(self, vals: List[int], target: int) -> tuple[int, int]:
        l, r = 0, len(vals) - 1
        while l < r:
            sum = vals[l] + vals[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return (l + 1, r + 1)
