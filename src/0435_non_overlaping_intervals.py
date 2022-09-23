from typing import *
# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        s_intervals = sorted(intervals)
        result = 0
        if s_intervals:
            prev = s_intervals[0]
            for inter in s_intervals[1:]:
                if inter[0] < prev[1]:
                    result += 1
                    if inter[1] < prev[1]:
                        prev = inter
                else: 
                    prev = inter
        return result

from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = [
        ([], 0),
        ([[1,2],[2,3],[3,4],[1,3]], 1),
        ([[1,2],[1,2],[1,2]], 2),
        ([[1,2],[2,3]], 0),
        ([[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]], 4),
        ([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]], 7),
    ]

    def testCases_eraseOverlapIntervals(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.eraseOverlapIntervals(nums)
                # assert
                self.assertEqual(expected, result, (nums))

if __name__ == '__main__':
    unittest.main()
