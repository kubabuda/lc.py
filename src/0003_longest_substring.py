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

    def lengthOfLongestSubstring_brute(self, s: str) -> int:
        i = 0
        maxL = 0
        while i < len(s):
            used = {}
            j = i
            while j < len(s) and s[j] not in used:
                used[s[j]] = True
                j += 1
                maxL = max(maxL, j - i)
            i += 1
        return maxL

    def lengthOfLongestSubstring_twoPointers(self, s: str) -> int:
        maxL = 0
        l = 0
        r = 0
        used = {}

        while r < len(s):
            while r < len(s) and s[r] not in used:
                used[s[r]] = r
                r += 1
                maxL = max(maxL, r - l)
            while r < len(s) and s[r] in used:
                del used[s[l]]
                l += 1

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
        ('dvdf', 3)
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


    def testCases_lengthOfLongestSubstring_brute(self):
        for word, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.lengthOfLongestSubstring_brute(word)
                # assert
                self.assertEqual(expected, result, (word))
    

    def testCases_lengthOfLongestSubstring_twoPointers(self):
        for word, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.lengthOfLongestSubstring_twoPointers(word)
                # assert
                self.assertEqual(expected, result, (word))

if __name__ == '__main__':
    unittest.main()
