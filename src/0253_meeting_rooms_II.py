from typing import *
# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-II
# https://www.lintcode.com/problem/919

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # O(n log n) time
        intervals.sort()
        result = 0
        start = 0
        end = 0
        while start < len(intervals):
            if start >= end or (end + 1 < len(intervals) and intervals[end + 1][0] < intervals[start][1]):
                end += 1
            else:
                start += 1
            result = max(result, end - start)
        return result
        
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        # O(n**2) time pessimistic
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

    def testCases_minMeetingRooms2(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.minMeetingRooms2(nums)
                # assert
                self.assertEqual(expected, result, (nums))

if __name__ == '__main__':
    unittest.main()
