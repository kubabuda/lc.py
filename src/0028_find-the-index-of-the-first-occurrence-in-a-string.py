from typing import *
# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lha, lne = len(haystack), len(needle)
        for i in range(lha):
            k = 0
            print(haystack, needle, i, k)
            while i+k < lha and k < lne and haystack[i+k] == needle[k]:
                k += 1
                if k >= lne:
                    return i
        return -1


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto",-1),
        ("a", "a", 0)
    ]

    def testCases_strStr(self):
        for hay, needle, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.strStr(hay, needle)
                # assert
                self.assertEqual(expected, result, (hay, needle))


if __name__ == '__main__':
    unittest.main()
