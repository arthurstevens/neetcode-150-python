# Problem: https://leetcode.com/problems/valid-anagram/
# NeetCode 150 – Arrays & Hashing
# Difficulty: Easy
# Time: O(n + m) simplifying to O(n), Space: O(1)


class Solution:
    """
    Hash table solution (array of size 26)
	
    Pros:
    - Faster and more memory efficient (constant space)
    - Single pass for both strings improves cache locality
	
    Cons:
    - Limited to lowercase English letters ('a'-'z')
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = [0] * 26
        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
            letters[ord(t[i]) - ord('a')] -= 1
            
        return letters == [0] * 26

class Solution:
    """
    Hash map solution (dictionary)
    
    Pros:
    - Works for any Unicode characters

    Cons:
    - Slightly slower due to hash lookup and dynamic memory allocation
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}
        for c in s:
            letters[c] = 1 + letters.get(c, 0)
                
        for c in t:
            if letters.get(c, 0) == 0:
                return False
            letters[c] -= 1
            
        return True