from typing import *
import heapq
# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for n in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, n)
            elif minheap[0] < n:
                heapq.heappushpop(minheap, n)
        return minheap[0]


import unittest

class SolutionTests(unittest.TestCase): 
        
    param_list = lambda _:[
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
    ]

    def testCases_findKthLargest(self):
        for nums, k, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findKthLargest(nums, k)
                # assert
                self.assertEqual(expected, result, (nums, k))

if __name__ == '__main__':
    unittest.main()
