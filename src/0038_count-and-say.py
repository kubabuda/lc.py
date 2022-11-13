from typing import *
# 38. Count and Say
# https://leetcode.com/problems/count-and-say

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        cs = self.countAndSay(n-1)
        res = []
        for c in cs:
            if not res or res[-1][0] != c:
                res.append([c,0])
            res[-1][1] += 1
        return "".join(f"{r[1]}{r[0]}" for r in res)


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        (1, "1"),
        (4, "1211"),
    ]

    def testCases_countAndSay(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.countAndSay(nums)
                # assert
                self.assertEqual(expected, result, (nums))


if __name__ == '__main__':
    unittest.main()
