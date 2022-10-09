from typing import *
# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isValid(self, s: str) -> bool:
        orda, ordz, ord0, ord9 = ord('a'), ord('z'), ord('0'), ord('9')

        def isAlfanumeric(c):
            ordc = ord(c)
            if orda <= ordc <= ordz: return True
            if ord0 <= ordc <= ord9: return True
            return False

        s = [c for c in s.lower() if isAlfanumeric(c)]
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: 
                return False
            l += 1
            r -= 1
        return True


from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        ("abba", True),
        ("aba", True),
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("race car", True),
        (" ", True),
        ("0P", False),
    ]

    def testCases_isValid(self):
        for s, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.isValid(s)
                # assert
                self.maxDiff = None
                self.assertEqual(result, expected, (s))

if __name__ == '__main__':
    unittest.main()
