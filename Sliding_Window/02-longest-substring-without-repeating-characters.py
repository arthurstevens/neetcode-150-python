# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# NeetCode 150 – Sliding Window
# Difficulty: Medium
# Time: O(n), Space: O(n)

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		l = maxL = 0
		subset = set()
		for r in range(len(s)):
			while s[r] in subset:
				subset.remove(s[l])
				l += 1
			subset.add(s[r])
			maxL = max(maxL, r - l + 1)
		return maxL
