from typing import *
import heapq
# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream

class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        
    def _is_even(self):
        return (len(self.minheap) + len(self.maxheap)) % 2 == 0

    def addNum(self, num: int) -> None:
        if not self.minheap or num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
            while len(self.minheap) > len(self.maxheap) + 1:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        else:
            heapq.heappush(self.maxheap, -num)
            while len(self.maxheap) > len(self.minheap) + 1:
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self) -> float:
        if self._is_even():
            result = (self.minheap[0] - self.maxheap[0]) / 2
        else:
            if len(self.minheap) > len(self.maxheap):
                result = self.minheap[0]
            else:
                result = -self.maxheap[0]
        return result


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
