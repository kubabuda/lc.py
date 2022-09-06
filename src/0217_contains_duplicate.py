from typing import *
# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for i in nums:
            if i in numsSet:
                return True
            numsSet.add(i)
        return False

from unittest import TestCase
import unittest

class Test(unittest.TestCase): 

    def testCases(self):
        param_list = [
            ([1,2,3,1], True),
            ([1,2,3,4], False),
            ([1,1,1,3,3,4,3,2,4,2], True)
        ]
        for nums, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.containsDuplicate(nums)
                # assert
                self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
