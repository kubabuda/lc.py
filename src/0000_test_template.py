from typing import *
# "title".toLocaleLowerCase().replaceAll(".","").replaceAll(" ", "_").replaceAll("-","_");
# https://leetcode.com/problems/

class Solution:
    def method(self, nums):
        return []


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ([], []),
    ]

    def testCases_method(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.method(nums)
                # assert
                self.assertEqual(expected, result, (nums))


if __name__ == '__main__':
    unittest.main()
