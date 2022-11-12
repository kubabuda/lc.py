from typing import *
# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """O((m+n) log(m+n)) time but no TLE"""
        nums = sorted(nums1 + nums2)
        mid = len(nums) // 2
        if not len(nums) % 2:
            return (nums[mid] + nums[mid-1]) / 2
        return nums[mid]


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ([1,3], [2], 2.00000),
        ([1,2], [3,4], 2.50000),
        ([], [2,3], 2.50000),
        ([1,2,3,4,5], [], 3.00000),
    ]

    def testCases_findMedianSortedArrays(self):
        for nums1, nums2, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findMedianSortedArrays(nums1, nums2)
                # assert
                self.assertEqual(expected, result, (nums1, nums2))


if __name__ == '__main__':
    unittest.main()
