from typing import *
# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = { c:0 for c in s }
        if len(counts) == 1: return len(s)
        maxL = 0
        left = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            maxL = max((right - left + 1), maxL)
        return maxL

    def characterReplacementF(self, s: str, k: int) -> int:
        counts = { }
        maxL = maxF = left = 0

        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)
            maxF = max(maxF, counts[s[right]])
            while (right - left + 1) - maxF > k:
                counts[s[left]] -= 1
                left += 1
            maxL = max((right - left + 1), maxL)
        return maxL


from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        ("AA", 2, 2),
        ("AAAA", 2, 4),
        ("AAAA", 0, 4),
        ("AAAB", 0, 3),
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("ABBA", 1, 3),
        ("ABBA", 0, 2),
        ("ABAA", 0, 2),
    ]

    def testCases_characterReplacement(self):
        for word, k, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.characterReplacement(word, k)
                # assert
                self.assertEqual(expected, result, (word, k))
    
    def testCases_characterReplacementF(self):
        for word, k, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.characterReplacementF(word, k)
                # assert
                self.assertEqual(expected, result, (word, k))

if __name__ == '__main__':
    unittest.main()
