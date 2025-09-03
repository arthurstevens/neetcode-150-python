# Problem: https://leetcode.com/problems/trapping-rain-water/
# NeetCode 150 – Two Pointers
# Difficulty: Easy/Medium/Hard
# Time: O(n), Space: O(1)

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        while l <= r:
            if height[l] < height[r]:
                l_max = max(l_max, height[l])
                trapped_water += l_max - height[l]
                l += 1
            else:
                r_max = max(r_max, height[r])
                trapped_water += r_max - height[r]
                r -= 1

        return trapped_water
