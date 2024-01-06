from typing import *
# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    # DFS with cache - top-down DP: O(N**2) time, O(N) space
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i: int) -> int:
            gt = None
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    gt = cache[j] if j in cache else dfs(j)
            result = 1
            if gt:
                result += gt
            cache[i] = result
            return result

        return max(dfs(i) for i in range(0, len(nums)))

    # bottom-up DP: O(N**2) time, O(N) memory
    def lengthOfLIS_DP(self, nums: List[int]) -> int:
        lis = [1 for i in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)
        return max(lis)

import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ([10,9,2,5,3,7,101,18], 4),
        ([0,1,0,3,2,3], 4),
        ([7,7,7,7,7,7,7], 1)
    ]

    def testCases_lengthOfLIS(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.lengthOfLIS(nums)
                # assert
                self.assertEqual(expected, result, (nums))

    def testCases_lengthOfLIS_DP(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.lengthOfLIS_DP(nums)
                # assert
                self.assertEqual(expected, result, (nums))


if __name__ == '__main__':
    unittest.main()
