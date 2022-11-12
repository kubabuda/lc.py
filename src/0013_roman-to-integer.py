from typing import *
# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        values = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, }
        res = 0

        for i, c in enumerate(s):
            val = values[c]
            if i+1 < len(s) and val < values[s[i+1]]:
                res -= val
            else:
                res += val

        return res


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994)
    ]

    def testCases_romanToInt(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.romanToInt(nums)
                # assert
                self.assertEqual(expected, result, (nums))

if __name__ == '__main__':
    unittest.main()
