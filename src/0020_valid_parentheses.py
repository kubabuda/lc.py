from typing import *
# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        par = { 
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
        opened = []

        for c in s:
            if c in par: opened.append(c)
            else:
                if not opened: return False
                last = opened.pop()
                if par[last] not c: return False
        return not opened



import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
    ]

    def testCases_isValid(self):
        for strs, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.isValid(strs)
                # assert
                self.maxDiff = None
                self.assertEqual(result, expected, (strs))

if __name__ == '__main__':
    unittest.main()
