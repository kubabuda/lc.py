from typing import *
# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-II
# https://www.lintcode.com/problem/919

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result = 0
        overlaps = []
        for meeting in intervals:
            for ov in overlaps: 
                if ov[1] <= meeting[0]:
                    overlaps.remove(ov)
            overlaps.append(meeting)
            result = max(result, len(overlaps))
        return result


from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase):
    
    param_list = [
        ([(0,30),(5,10),(15,20)], 2),
        ([(2,7)], 1),
    ]

    def testCases_minMeetingRooms(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.minMeetingRooms(nums)
                # assert
                self.assertEqual(expected, result, (nums))

if __name__ == '__main__':
    unittest.main()
