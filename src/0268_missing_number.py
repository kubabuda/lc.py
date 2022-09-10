from typing import *
# https://leetcode.com/problems/missing-number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        act_sum = sum(nums)
        orig_len = len(nums) + 1
        exp_sum = int(len(nums) * orig_len / 2)
        return exp_sum - act_sum

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    def testCases(self):
        param_list = [
            ([0,1], 2),
            ([0,1,3], 2),
            ([0,1,2], 3),
            ([0,1,2,4], 3),
            ([0,1,2,3], 4),
        ]
        for nums, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.missingNumber(nums)
                # assert
                self.assertEqual(expected, result, (nums))

if __name__ == '__main__':
    unittest.main()
