# Problem: https://leetcode.com/problems/valid-palindrome/
# NeetCode 150 – Two Pointers
# Difficulty: Easy
# Time: O(n), Space: O(1)

# Faster with built-in alphanumeric check
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum(): l += 1
            while r > l and not s[r].isalnum(): r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


# Slower with custom alphanumeric check
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlphanumeric(s[l]): l += 1
            while r > l and not self.isAlphanumeric(s[r]): r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isAlphanumeric(self, s: chr) -> bool:
        return (
            ord('A') <= ord(s) <= ord('Z') or
            ord('a') <= ord(s) <= ord('z') or
            ord('0') <= ord(s) <= ord('9')
        )
