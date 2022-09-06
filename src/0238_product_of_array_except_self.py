from typing import *
# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time O(n) memory
        result = [1 for i in nums]
        for i in range(0, len(nums) - 1):
            result[i + 1] = result[i] * nums[i]

        rmul = [1 for i in nums]
        for i in reversed(range(1, len(nums))):
            rmul[i - 1] = nums[i] * rmul[i]

        for i, r in enumerate(result):
            result[i] = r * rmul[i]

        return result


from unittest import TestCase
import unittest

class Test(unittest.TestCase): 
    
    def testCases(self):
        param_list = [
            ([1,2,3,4], [24,12,8,6]),
            ([-1,1,0,-3,3], [0,0,9,0,0]),
        ]
        for nums, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.productExceptSelf(nums)
                # assert
                self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
