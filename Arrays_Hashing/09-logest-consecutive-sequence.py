# Problem: https://leetcode.com/problems/longest-consecutive-sequence/
# NeetCode 150 – Arrays & Hashing
# Difficulty: Medium
# Time: O(), Space: O()

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        collection = set(nums)
        topCount = 0
        for n in collection:
            if (n - 1) in collection:
                continue
            count = 1
            while (n + count) in collection:
                count += 1
            topCount = max(topCount, count)
        return topCount