from typing import *
# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j, n in enumerate(nums):
            if i == 0 or n != nums[i-1]:
                nums[i] = n
                i += 1
        while len(nums) > i:
            nums.pop()

        return len(nums)


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ([1,1,2], 2, [1,2]),
        ([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4]),
    ]

    def testCases_removeDuplicates(self):
        for nums, exp_result, exp_nums in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.removeDuplicates(nums)
                # assert
                self.assertEqual(exp_result, result)
                self.assertEqual(exp_nums, nums)


if __name__ == '__main__':
    unittest.main()
