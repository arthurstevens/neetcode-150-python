# Problem: https://leetcode.com/problems/valid-parentheses/
# NeetCode 150 – Stack
# Difficulty: Easy
# Time: O(n), Space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis_open = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        for c in s:
            if c in parenthesis_open:
                if stack and stack[-1] == parenthesis_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
