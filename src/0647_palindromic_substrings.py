from typing import *
# 0647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        "O(n**2) time O(1) space"
        result, N = 0, len(s)
        for i in range(N):
            l = r = i
            while l >= 0 and r < N and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
            l = i
            r = l + 1
            while l >= 0 and r < N and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
        return result



import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        ("abba", 6),
        ("aba", 4),
        ("abc", 3),
        ("a", 1),
        ("aaa", 6),
    ]

    def testCases_countSubstrings(self):
        for s, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.countSubstrings(s)
                # assert
                self.assertEqual(result, expected, s)


if __name__ == '__main__':
    unittest.main()
