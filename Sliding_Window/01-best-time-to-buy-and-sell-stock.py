# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# NeetCode 150 – Sliding Window
# Difficulty: Easy
# Time: O(n), Space: O(1)

from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		if len(prices) <= 1:
			return 0
			
		l, r = 0, 1
		maxP = 0
		while r < len(prices):
			if prices[l] < prices[r]:
				max(maxP, prices[r] - prices[l])
			else:
				l = r
			r += 1
		return maxP
