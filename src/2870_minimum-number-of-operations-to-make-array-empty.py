from typing import *
# 2870. Minimum Number of Operations to Make Array Empty
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = {}
        for n in nums:
            if n not in cnt:
                cnt[n] = 0
            cnt[n] += 1
        for n in cnt:
            if cnt[n] < 2:
                return -1
        result = 0
        for n in cnt:
            while cnt[n] > 0:
                if cnt[n] == 2 or cnt[n] == 4:
                    cnt[n] -= 2
                else:
                    cnt[n] -= 3
                result += 1
        return result


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ([2,3,3,2,2,4,2,3,4], 4),
        ([2,1,2,2,3,3], -1)
    ]

    def testCases_minOperations(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.minOperations(nums)
                # assert
                self.assertEqual(expected, result, (nums))


if __name__ == '__main__':
    unittest.main()
