from typing import *
# https://leetcode.com/problems/maximum-subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        maxSum = currentSum
        for i in nums[1:]:
            currentSum = max(i, currentSum + i)
            maxSum = max(maxSum, currentSum)
        return maxSum



import unittest

class Test(unittest.TestCase): 
    
    def testCases(self):
        param_list = [
            ([-2,1,-3,4,-1,2,1,-5,4], 6),
            ([1], 1),
            ([5,4,-1,7,8], 23),
            ([1,2,3,4], 10),
            ([1,2,-1,-2,2,1,-2,1,4,-5,4], 6),
        ]
        for nums, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.maxSubArray(nums)
                # assert
                self.assertEqual(expected, result, nums)

if __name__ == '__main__':
    unittest.main()
