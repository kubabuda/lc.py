from typing import *
# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []
        if intervals:
            result.append(intervals[0])
            for inter in intervals[1:]:
                if inter[0] <= result[-1][1]: # merge
                    result[-1][1] = max(inter[1], result[-1][1])
                else:   # add new interval
                    result.append(inter)
        return result


import unittest

class SolutionTests(unittest.TestCase): 

    param_list = [
        ([], []),
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
    ]

    def testCases_merge(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.merge(nums)
                # assert
                self.assertEqual(expected, result, (nums))

if __name__ == '__main__':
    unittest.main()
