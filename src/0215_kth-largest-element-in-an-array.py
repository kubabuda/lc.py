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

    def findKthLargestQuickSelect(self, nums: List[int], k: int) -> int:
        ki = len(nums) - k
        
        def quickSelect(l, r):
            pivotVal, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivotVal:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > ki:   return quickSelect(l, p - 1)
            elif p < ki: return quickSelect(p + 1, r)
            else:       return nums[p]

        return quickSelect(0, len(nums) - 1) 

    def findKthLargestNaive(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return nums[-k]


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

    def testCases_findKthLargestQuickSelect(self):
        for nums, k, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findKthLargestQuickSelect(nums, k)
                # assert
                self.assertEqual(expected, result, (nums, k))

    def testCases_findKthLargest(self):
        for nums, k, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findKthLargestNaive(nums, k)
                # assert
                self.assertEqual(expected, result, (nums, k))

if __name__ == '__main__':
    unittest.main()
