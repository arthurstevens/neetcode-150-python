# Problem: https://leetcode.com/problems/longest-repeating-character-replacement/
# NeetCode 150 – Sliding Window
# Difficulty: Medium
# Time: O(), Space: O()

class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		l = 0
		maxL = 0
		maxF = 0
		chrs = [0] * 26
		for r in range(len(s)):
			chrs[ord(s[r]) - ord('A')] += 1
			maxF 
			while r - l + 1 - max(chrs) > k:
				chrs[ord(s[l]) - ord('A')] -= 1
				l += 1
			maxL = max(maxL, r - l + 1)
		return(maxL)
