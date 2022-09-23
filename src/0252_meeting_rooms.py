from typing import *
# 252. Meeting Rooms
# https://leetcode.com/problems/meeting-rooms
# https://www.lintcode.com/problem/920/

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if intervals:
            prev_end = intervals[0][1]
            for start,end in intervals[1:]:
                if start < prev_end:
                    return False
                prev_end = end
        return True

from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = [
        ([(0,30),(5,10),(15,20)], False),
        ([(5,8),(9,15)], True),
    ]

    def testCases_canAttendMeetings(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.canAttendMeetings(nums)
                # assert
                self.assertEqual(expected, result, (nums))

if __name__ == '__main__':
    unittest.main()
