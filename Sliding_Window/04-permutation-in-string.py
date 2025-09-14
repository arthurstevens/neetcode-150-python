# Problem: https://leetcode.com/problems/permutation-in-string/
# NeetCode 150 – Sliding Window
# Difficulty: Medium
# Time: O(n), Space: O(1)

# Optimal solution utilising a matches counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        idx_base = ord('a')
        s1_set = [0] * 26
        window_set = [0] * 26

        matches = 26
        for c in s1:
            i = ord(c) - idx_base
            if s1_set[i] == 0:
                matches -= 1
            s1_set[i] += 1

        l = 0
        for r in range(len(s2)):
            i = ord(s2[r]) - idx_base
            if window_set[i] == s1_set[i]:
                matches -= 1
            elif window_set[i] + 1 == s1_set[i]:
                matches += 1
            window_set[i] += 1

            if r - l + 1 > len(s1):
                i = ord(s2[l]) - idx_base
                if window_set[i] == s1_set[i]:
                    matches -= 1
                elif window_set[i] - 1 == s1_set[i]:
                    matches += 1
                window_set[i] -= 1
                l += 1

            if matches == 26:
                return True

        return False

# Simpler solution for more readability, negligible performance difference but technically slower
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        idx_base = ord('a')
        s1_set = [0] * 26
        window_set = [0] * 26

        for c in s1:
            s1_set[ord(c) - idx_base] += 1

        l = 0
        for r in range(len(s2)):
            window_set[ord(s2[r]) - idx_base] += 1

            if r - l + 1 > len(s1):
                window_set[ord(s2[l]) - idx_base] -= 1
                l += 1

            if r - l + 1 == len(s1) and window_set == s1_set:
                return True

        return False