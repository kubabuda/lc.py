from typing import *
# https://leetcode.com/problems/maximum-product-subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = currMax
        allMax = currMax
        
        for n in nums[1:]:
            curr = [n, currMax * n, currMin * n]
            currMin = min(curr)
            currMax = max(curr)
            allMax = max(allMax, currMax)
        return allMax


from unittest import TestCase
import unittest

class Test(unittest.TestCase): 
    
    def testCases(self):
        param_list = [
            ([2,3,-2,4], 6),
            ([1], 1),
            ([-2, 0, -1], 0),
        ]
        for nums, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.maxProduct(nums)
                # assert
                self.assertEqual(expected, result, nums)

if __name__ == '__main__':
    unittest.main()
