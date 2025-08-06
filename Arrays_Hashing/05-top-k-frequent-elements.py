# Problem: https://leetcode.com/problems/top-k-frequent-elements/
# NeetCode 150 – Arrays & Hashing
# Difficulty: Medium
# Time: O(n), Space: O(n)

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)
        
        buckets = [[] for _ in range (len(nums) + 1)]
        for val, freq in freq_map.items():
            buckets[freq].append(val)
            
        top_k = []
        for i in range(len(nums), 0, -1):
            if buckets[i]:
                top_k.extend(buckets[i])
            if len(top_k) >= k:
                break
            
        return top_k[:k]
