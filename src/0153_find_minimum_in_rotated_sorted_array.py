from typing import *
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        begin = 0
        end = len(nums) - 1

        while begin < end:
            mid = int((begin + end) / 2)
            if nums[mid] > nums[end]: # target on right half
                begin = mid + 1
            else: # target on left half
                end = mid - 1
        return nums[begin]


from unittest import TestCase
import unittest

class Test(unittest.TestCase): 
    
    def testCases(self):
        param_list = [
            ([3,4,5,1,2], 1),
            ([4,5,6,7,0,1,2], 0),
            ([11,13,15,17], 11),
        ]
        for nums, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findMin(nums)
                # assert
                self.assertEqual(expected, result, nums)

if __name__ == '__main__':
    unittest.main()
