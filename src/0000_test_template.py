from typing import *
# https://leetcode.com/problems/

class Solution:
    def method(self, nums):
        return []

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    
    def test(self):
        # arrange
        s = Solution()
        # act
        result = 2
        # assert
        self.assertEqual(2, result)
    
    param_list = [
        ([], []),
    ]

    def testCases(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.method(nums)
                # assert
                self.assertEqual(expected, result, (nums))

if __name__ == '__main__':
    unittest.main()
