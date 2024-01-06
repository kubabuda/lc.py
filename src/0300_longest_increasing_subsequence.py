from typing import *
# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    # bruteforce DFS
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i: int) -> int:
            gte = [cache[j] if j in cache else dfs(j)
                for j in range(i+1, len(nums)) 
                if nums[j] > nums[i]]
            result = 1
            if gte:
                result += max(gte)
            cache[i] = result
            return result

        return max(dfs(i) for i in range(0, len(nums)))


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


if __name__ == '__main__':
    unittest.main()
