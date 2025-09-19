# Problem: https://leetcode.com/problems/minimum-window-substring/
# NeetCode 150 – Sliding Window
# Difficulty: Hard
# Time: O(), Space: O()

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        t_count, w_count = Counter(t), defaultdict(int)
        chrs_have, chrs_need = 0, len(t_count)
        res, res_len = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            w_count[c] += 1

            if c in t_count and w_count[c] == t_count[c]:
                chrs_have += 1

            while chrs_have == chrs_need:
                if r - l + 1 < res_len:
                    res, res_len = [l, r], r - l + 1

                w_count[s[l]] -= 1
                if s[l] in t_count and w_count[s[l]] + 1 == t_count[s[l]]:
                    chrs_have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
