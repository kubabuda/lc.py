from typing import *

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        for i1, n1 in enumerate(height[:-1]):
            for i2, n2 in enumerate(height[(i1+1):]):
                h = min(n1, n2)
                l = i2 + 1
                area = h * l
                maxArea = max(area, maxArea)
        return maxArea


    def maxAreaBruteforce(self, height: List[int]) -> int:
        maxArea = 0
        for i1, n1 in enumerate(height[:-1]):
            for i2, n2 in enumerate(height[(i1+1):]):
                h = min(n1, n2)
                l = i2 + 1
                area = h * l
                maxArea = max(area, maxArea)
        return maxArea

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    def testCases(self):
        param_list = [
            ([1,8,6,2,5,4,8,3,7], 49),
            ([1,1], 1),
        ]
        for nums, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.maxArea(nums)
                # assert
                self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
