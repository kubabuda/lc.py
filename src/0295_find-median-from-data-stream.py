from typing import *
import heapq
# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream

class MedianFinder:

    def __init__(self):
        self.larger = []
        self.lower = []

    def addNum(self, num: int) -> None:
        if not self.larger or num > self.larger[0]:
            heapq.heappush(self.larger, num)
        else:
            heapq.heappush(self.lower, -num)
        
        if len(self.larger) > len(self.lower) + 1:
            heapq.heappush(self.lower, -heapq.heappop(self.larger))
        if len(self.lower) > len(self.larger) + 1:
            heapq.heappush(self.larger, -heapq.heappop(self.lower))

    def findMedian(self) -> float:
        if len(self.larger) > len(self.lower):
            return self.larger[0]
        elif len(self.larger) == len(self.lower):
            return (self.larger[0] - self.lower[0]) / 2
        return -self.lower[0]


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        (["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
         [[],               [1],    [2],      [],           [3],      []],
         [null,             null,   null,     1.5,          null,     2.0]),
        (["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"],
         [[],            [-1],     [],          [-2],    [],         [-3],     [],         [-4],    [],          [-5],    []],
         [null,          null,     -1.00000,    null,    -1.50000,   null,     -2.00000,   null,    -2.50000,    null,    -3.00000]),
    ]

    def testCases_method(self):
        for cmds, params, expected in self.param_list():
            with self.subTest():
                # arrange
                obj = MedianFinder()
                result = []
                for cmd, param in zip(cmds, params):
                    res = null
                    if cmd == "MedianFinder":
                        obj = MedianFinder()
                    elif cmd == "addNum":
                        # act
                        obj.addNum(param[0])
                    elif cmd == "findMedian":
                        res = obj.findMedian()
                    result.append(res)
                # assert
                self.assertEqual(expected, result, (cmds, params))

if __name__ == '__main__':
    unittest.main()
