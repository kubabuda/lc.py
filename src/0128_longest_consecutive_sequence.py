from typing import *
# from collections import deque
# https://leetcode.com/problems/course-schedule/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums_set = set(nums)
        max_l = 1
        
        for n in nums:
            prev = n - 1
            if prev not in nums_set:
                curr_l = 1

                next = n + 1
                while next in nums_set:
                    n = next
                    curr_l += 1
                    next = n + 1

                max_l = max(curr_l, max_l)
        
        return max_l

        

import unittest
class SolutionTests(unittest.TestCase): 
    
    param_list = [
        ([], 0),
        ([0], 1),
        ([0,3,7,2,5,8,4,6,0,1], 9),
        ([100,4,200,1,3,2], 4),
        ([0,1,2,4,8,5,6,7,9,3,55,88,77,99,999999999], 10)
    ]

    def testCases(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.longestConsecutive(nums)
                # assert
                self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
