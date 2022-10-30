from typing import *
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_i = { num: i for i, num in enumerate(nums) }
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_i:
                j = nums_i[diff]
                if j != i:
                    return [i, j]
        return [-1, -1]



import unittest

class TestSum(unittest.TestCase): 
    def test(self):
        # arrange
        s = Solution()
        # act
        result = s.twoSum([1,2,3], 5)
        # assert
        self.assertEqual([1, 2], result)
    
    def testCases(self):
        param_list = [
            ([2,7,11,15], 9, [0, 1]),
            ([3,2,4], 6, [1,2]),
            ([3,3], 6, [0,1])
        ]
        for nums, target, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.twoSum(nums, target)
                # assert
                self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
