from typing import *

# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion

class Solution:
    '''O(N) time O(N) space'''
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lines = [[] for i in range(numRows)]
        p = numRows * 2 - 2
        for i, c in enumerate(s):
            j = i % p
            if j >= numRows:
                j = p - j
            lines[j].append(c)
        return ''.join([''.join(l) for l in lines])
    

import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A")
    ]

    def testCases_convert(self):
        for s, numRows, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.convert(s, numRows)
                # assert
                self.assertEqual(expected, result, (s, numRows))

if __name__ == '__main__':
    unittest.main()
