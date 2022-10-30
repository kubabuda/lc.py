from typing import *
# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev = {}
        maxL = 0
        start = 0
        for i in range(len(s)):
            c = s[i]
            if c in prev:
                start = max(start, prev[c] + 1)
            prev[c] = i
            maxL = max(i + 1 - start, maxL)
        return maxL



import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda _: [
        ('a', 1),
        (' ', 1),
        ('aa', 1),
        ('ab', 2),
        ('bbbbb', 1),
        ('abcabcbb', 3),
        ('pwwkew', 3),
        ('abba', 2),
        ('abb', 2),
    ]

    def testCases_lengthOfLongestSubstring(self):
        for word, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.lengthOfLongestSubstring(word)
                # assert
                self.assertEqual(expected, result, (word))

if __name__ == '__main__':
    unittest.main()
