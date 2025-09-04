# Problem: https://leetcode.com/problems/container-with-most-water/
# NeetCode 150 – Two Pointers
# Difficulty: Medium
# Time: O(n), Space: O(1)

from typing import List


class Solution:
	def maxArea(self, height: List[int]) -> int:
		l, r = 0, len(height) - 1
		max_vol = None
		while l < r:
			max_vol = max(min(height[l], height[r]) * (r - l), max_vol)
			if height[l] > height[r]:
				r -= 1
			else:
				l += 1
		return max_vol
		