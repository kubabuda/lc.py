from typing import *
# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc,tc = Counter(s), Counter(t)
        if len(sc) != len(tc): return False
        for c in sc:
            if c not in tc or tc[c] != sc[c]: return False
        return True



import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda _: [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False),
        ("abc", "ab", False),
    ]

    def testCases_isAnagram(self):
        for s, t, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.isAnagram(s, t)
                # assert
                self.assertEqual(expected, result, (s, t))

if __name__ == '__main__':
    unittest.main()
