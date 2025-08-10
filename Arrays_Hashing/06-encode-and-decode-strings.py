# Problem: https://leetcode.com/problems/encode-and-decode-strings/
# NeetCode 150 – Arrays & Hashing
# Difficulty: Medium
# Encode:
#   Time: O(n), Space: O(n)
# Decode:
#   Time: O(n), Space: O(n)

from typing import List


class Solution:
    """
    Entirely for fun creative approach, light obfuscation
    RLE wrapped in a double caeser cipher
    """
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        shifted = [self._unicodeShift(s, 10) for s in strs]
        rle = [self._runLengthEncode(s) for s in shifted]
        compressed = ''.join(f'{len(s)}:{s}' for s in rle)
        return self._unicodeShift(compressed, 10)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        parsed = []
        i = 0
        s = self._unicodeShift(s, -10)
        while i < len(s):
            j = s.index(':', i)
            length = int(s[i:j])
            start = j + 1
            rle = self._runLengthDecode(s[start:start+length])
            parsed.append(self._unicodeShift(rle, -10))
            i = start + length
        return parsed
    
    def _unicodeShift(self, s: str, shift: int) -> str:
        UNICODE_MAX = 0x110000
        return ''.join(chr((ord(c) + shift) % UNICODE_MAX) for c in s)
    
    def _runLengthEncode(self, s: str) -> str:
        rle = []
        i = 0
        while i < len(s):
            count = 1
            while i + count < len(s) and s[i + count] == s[i]:
                count += 1
            rle.append(f'{ord(s[i])}|{count}')
            i += count
        return ','.join(rle)

    def _runLengthDecode(self, s: str) -> str:
        if not s:
            return ''
        decoded = []
        tokens = s.split(',')
        for token in tokens:
            char_code, count = token.split('|')
            decoded.append(chr(int(char_code)) * int(count))
        return ''.join(decoded)
