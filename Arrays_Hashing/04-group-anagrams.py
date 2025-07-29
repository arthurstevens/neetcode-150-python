# Problem: https://leetcode.com/problems/group-anagrams/
# NeetCode 150 – Arrays & Hashing
# Difficulty: Medium

from typing import List
from collections import defaultdict


# Time: O(n * m log m), Space: O(n)
class Solution:
    """
    Hashmap & sort for key
    
    Pros:
    - Small performance loss (k log k) but outperforms for shorter strings
    - Works for any Unicode characters

    Cons:
    - Slightly slower due to hash lookup and dynamic memory allocation
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        groups = defaultdict(list)
        for word in strs:
            sort = ''.join(sorted(word))
            groups[sort].append(word)
            
        return list(groups.values())

# Time: O(n * m), Space: O(n)
class Solution:
    """
    Hashmap & array (len 26) as key
	
    Pros:
    - Suited to longer strings, uses constant space
	
    Cons:
    - Limited to lowercase English letters ('a'-'z')
    - Excessive operations for shorter strings
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        groups = defaultdict(list)
        for word in strs:
            chrs = [0] * 26
            for c in word:
                chrs[ord(c) - ord('a')] += 1
            groups[tuple(chrs)].append(word)
            
        return list(groups.values())
