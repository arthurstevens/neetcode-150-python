# Problem: https://leetcode.com/problems/min-stack/
# NeetCode 150 – Stack
# Difficulty: Medium
# Time: O(1) for all operations, Space: O(n)

from typing import Optional


# Two stacks
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    
# One stack (higher memory efficiency)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min is None:
            self.min = val
            self.stack.append(0)
        else:
            self.stack.append(val - self.min)
            self.min = min(val, self.min)

    def pop(self) -> None:
        if not self.stack: 
            return
        val = self.stack.pop()
        if val < 0:
            self.min -= val
        if not self.stack:
            self.min = None

    def top(self) -> Optional[int]:
        if self.min is None:
            return None
        val = self.stack[-1]
        if val > 0:
            return self.min + val
        else:
            return self.min
        
    def getMin(self) -> Optional[int]:
        return self.min
