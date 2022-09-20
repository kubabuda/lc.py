from typing import *
# https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        # add all non-overlaping intervals before new
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        start = newInterval[0]
        end = newInterval[1]
        if i < len(intervals) and end >= intervals[i][0]:
                start = min(start, intervals[i][0])
                while i + 1 < len(intervals) and end >= intervals[i + 1][0]:
                    i += 1  # ignore intervals overlapped by new one
                end = max(end, intervals[i][1])
                i += 1
        result.append([start, end])
        
        # add all non-overlaping intervals after new
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        return result

    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i, inter in enumerate(intervals):
            if inter[0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            elif inter[1] < newInterval[0]:
                result.append(inter)
            else:
                newInterval[0] = min(newInterval[0], inter[0])
                newInterval[1] = max(newInterval[1], inter[1])
        result.append(newInterval)
        
        return result

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 

    param_list = [
        ([], [2,5], [[2,5]]),
        ([[1,5]], [0,0], [[0,0],[1,5]]),
        ([[1,5]], [0,1], [[0,5]]),
        ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]]),
    ]

    def testCases_insert(self):
        for intervals, newInterval, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.insert(intervals, newInterval)
                # assert
                self.assertEqual(expected, result, (intervals, newInterval))

    def testCases_insert2(self):
        for intervals, newInterval, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.insert2(intervals, newInterval)
                # assert
                self.assertEqual(expected, result, (intervals, newInterval))


if __name__ == '__main__':
    unittest.main()
