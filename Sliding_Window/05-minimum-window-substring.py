# Problem: https://leetcode.com/problems/minimum-window-substring/
# NeetCode 150 – Sliding Window
# Difficulty: Hard

# Hashmap solution
# Time:  O(n + m) where n is len(s), m is len(t)
# Space: O(u) where u is unique characters in t
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        t_count, w_count = {}, {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        chrs_have, chrs_need = 0, len(t_count)
        res, res_len = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]

            if c in t_count:
                w_count[c] = 1 + w_count.get(c, 0)
                if w_count[c] == t_count[c]:
                    chrs_have += 1

            while chrs_have == chrs_need:
                if r - l + 1 < res_len:
                    res, res_len = [l, r], r - l + 1
                
                c = s[l]
                if c in t_count: 
                    w_count[c] -= 1
                    if w_count[c] < t_count[c]:
                        chrs_have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""

# Fixed-size array solution
# Time:  O(n + m) where n is len(s), m is len(t)
# Space: O(1)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        base = ord('A')  # 65
        size = ord('z') - base + 1  # 58
        
        t_count = [0] * size
        w_count = [0] * size
        
        for c in t:
            t_count[ord(c) - base] += 1
        
        chrs_have, chrs_need = 0, sum(1 for c in t_count if c > 0)
        res, res_len = [-1, -1], float('inf')
        l = 0
        
        for r, c in enumerate(s):
            ri = ord(c) - base
            w_count[ri] += 1
            
            if t_count[ri] > 0 and w_count[ri] == t_count[ri]:
                chrs_have += 1
            
            while chrs_have == chrs_need:
                if r - l + 1 < res_len:
                    res, res_len = [l, r], r - l + 1
                
                li = ord(s[l]) - base
                w_count[li] -= 1
                if t_count[li] > 0 and w_count[li] < t_count[li]:
                    chrs_have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
