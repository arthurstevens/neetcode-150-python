# Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# NeetCode 150 – Stack
# Difficulty: Medium
# Time: O(n), Space: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tok_stack = []

        for token in tokens:
            if token not in "+-*/":
                tok_stack.append(int(token))
                continue

            n2 = tok_stack.pop()
            n1 = tok_stack.pop()

            if token == "+": res = n1 + n2
            elif token == "-": res = n1 - n2
            elif token == "*": res = n1 * n2
            elif token == "/": res = n1 / n2

            tok_stack.append(int(res))

        return tok_stack[-1]
