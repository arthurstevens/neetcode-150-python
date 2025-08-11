# Problem: https://leetcode.com/problems/product-of-array-except-self/
# NeetCode 150 – Arrays & Hashing
# Difficulty: Medium
# Time: O(n), Space: O(1) extra space, O(n) for output array

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [0] * len(nums)
        pre, post = 1, 1
        for i in range(len(nums)):
            products[i] = pre
            pre *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= post
            post *= nums[i]
        return products
