# Problem: https://leetcode.com/problems/longest-repeating-character-replacement/
# NeetCode 150 – Sliding Window
# Difficulty: Medium
# Time: O(n), Space: O(1)

class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		l = maxL = maxF = 0
		chrs_base = ord('A')
		chrs = [0] * 26
		for r in range(len(s)):
			i = ord(s[r]) - chrs_base
			chrs[i] += 1
			maxF = max(maxF, chrs[i])
			while r - l + 1 - maxF > k:
				chrs[ord(s[l]) - ord('A')] -= 1
				l += 1
			maxL = max(maxL, r - l + 1)
		return(maxL)
