# Problem: https://leetcode.com/problems/contains-duplicate/
# NeetCode 150 – Arrays & Hashing
# Difficulty: Easy
# Time: O(n), Space: O(n)

from typing import List


class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		return len(set(nums)) != len(nums)
