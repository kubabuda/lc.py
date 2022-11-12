from typing import *
# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        s0 = strs[0]

        while True:
            k = len(result)
            if k >= len(s0): return result

            for s in strs:
                if k >= len(s) or s[k] != s0[k]: 
                    return result
            result = s0[:k+1]


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        (["flower","flow","flight"],"fl"),
        (["dog","racecar","car"], ""),
    ]

    def testCases_longestCommonPrefix(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.longestCommonPrefix(nums)
                # assert
                self.assertEqual(expected, result, (nums))

if __name__ == '__main__':
    unittest.main()
