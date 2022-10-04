from typing import *
# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uniqC = set((c for c in s))
        if len(uniqC) == 1: return len(s)
        maxL = 0
        for i,c in enumerate(uniqC):
            left = 0
            right = 0
            toRepl = 0
            while left < len(s):
                if right < len(s) and toRepl < k or right + 1 < len(s) and s[right] == c:
                    right += 1
                    if right < len(s) and s[right] != c:
                        toRepl += 1
                else:
                    if s[left] != c:
                        toRepl -= 1
                    left += 1
                maxL = max(right - left, maxL)
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

if __name__ == '__main__':
    unittest.main()
