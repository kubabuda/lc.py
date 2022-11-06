from typing import *
import heapq
# 703. Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.k = k
        for val in nums:
            self.add(val)

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
        elif self.minheap[0] < val:
            heapq.heappushpop(self.minheap, val)
        return self.minheap[0]


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    
    param_list = lambda _:[
        (["KthLargest", "add", "add", "add", "add", "add"],
         [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
         [null, 4, 5, 5, 8, 8]),
    ]

    def testCases_method(self):
        for cmds, params, expected in self.param_list():
            with self.subTest():
                # arrange
                obj = None
                results = []
                for i, cmd in enumerate(cmds):
                    if cmd == "KthLargest":
                        k, nums = params[i]
                        obj = KthLargest(k, nums)
                        results.append(null)
                    elif cmd == "add":
                        val = params[i][0]
                        # act
                        res = obj.add(val)
                        results.append(res)
                    # else: 
                    #     self.assertFalse(True, f"Fail: cmd#{i}={cmd} should never happen")
                # assert
                self.assertEqual(expected, results, (params[0]))

if __name__ == '__main__':
    unittest.main()
