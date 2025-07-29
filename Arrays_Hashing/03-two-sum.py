# Problem: https://leetcode.com/problems/two-sum/
# NeetCode 150 – Arrays & Hashing
# Difficulty: Easy
# Time: O(n), Space: O(n)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in indexMap:
                return [i, indexMap[diff]]
            else:
                indexMap[num] = i