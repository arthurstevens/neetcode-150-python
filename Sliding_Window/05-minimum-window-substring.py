# Problem: https://leetcode.com/problems/minimum-window-substring/
# NeetCode 150 – Sliding Window
# Difficulty: Hard
# Time: O(), Space: O()

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        
        l = 0
        res = ""
        s_count = defaultdict(int)
        for r in range(len(s)):
            s_count[s[r]] += 1
            while l < r and s_count[s[l]] > t_count[s[l]]:
                s_count[s[l]] -= 1
                l += 1
            
            
