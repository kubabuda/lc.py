from typing import *
# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        "O(n**2) time O(1) space"
        N = len(s)
        maxL, maxR, maxLen = 0, 0, 0
        for i in range(N):
            l = r = i
            while l >= 0 and r < N and s[l] == s[r]:
                if r - l > maxLen:
                    maxL, maxR = l, r
                    maxLen = r - l
                l -= 1
                r += 1
            l = i
            r = l + 1
            while l >= 0 and r < N and s[l] == s[r]:
                if r - l > maxLen:
                    maxL, maxR = l, r
                    maxLen = r - l
                l -= 1
                r += 1
        return s[maxL:maxR+1]


from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        ("abba", "abba"),
        ("aba", "aba"),
        ("abb", "bb"),
        ("abc", "a"),
        ("cbbd", "bb"),
    ]

    def testCases_longestPalindrome(self):
        for s, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.longestPalindrome(s)
                # assert
                self.assertEqual(len(result), len(expected), f'{s}: {result} != {expected}')
                self.assertTrue(result in s)


if __name__ == '__main__':
    unittest.main()