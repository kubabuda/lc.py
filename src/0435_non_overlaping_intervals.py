from typing import *
# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        overlaps = [ set() for i in intervals ]
        for i, inter in enumerate(intervals):
            j = i - 1
            while j > 0 and intervals[j][1] > intervals[i][0]:
                overlaps[i].add(j)
                overlaps[j].add(i)
                j -= 1
            j = i + 1
            while j < len(intervals) and intervals[j][0] < intervals[i][1]:
                overlaps[i].add(j)
                overlaps[j].add(i)
                j += 1
        act_overlaps = { i: o for i, o in enumerate(overlaps) if o }
        result = 0
        while act_overlaps:
            result += 1
            i = max(act_overlaps, key=lambda i: len(act_overlaps[i]))
            for j in act_overlaps[i]:
                act_overlaps[j].remove(i)
                if not act_overlaps[j]:
                    act_overlaps.pop(j)
            act_overlaps.pop(i)
        
        return result

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    
    param_list = [
        ([], 0),
        ([[1,2],[2,3],[3,4],[1,3]], 1),
        ([[1,2],[1,2],[1,2]], 2),
        ([[1,2],[2,3]], 0),
        ([[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]], 4)
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
