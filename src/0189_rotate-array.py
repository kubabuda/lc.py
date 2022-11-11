from typing import *
# 189. Rotate Array
# https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N
        rotnums = []
        for n in nums[N-k:]:
            rotnums.append(n)
        for n in nums[0:N-k]:
            rotnums.append(n)
        for i in range(N):
            nums[i] = rotnums[i]


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
        ([-1,-100,3,99], 2, [3,99,-1,-100]),
        ([1,2], 1, [2,1]),
        ([1,2], 2, [1,2]),
        ([1,2], 5, [2,1]),
    ]

    def testCases_rotate(self):
        for nums, k, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                numsIn = [i for i in nums]
                # act
                s.rotate(numsIn, k)
                # assert
                self.assertEqual(expected, numsIn, (nums, k))

    # def test(self):
    #     self.assertEqual(2, -1)

if __name__ == '__main__':
    unittest.main()
