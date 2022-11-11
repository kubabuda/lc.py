from typing import *
# 189. Rotate Array
# https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """O(n) time O(n) space
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

    def rotatePy(self, nums: List[int], k: int) -> None:
        N = len(nums)
        k = k % N
        rotnums = nums[N-k:] + nums[:N-k]
        for i in range(N):
            nums[i] = rotnums[i]

    def rotateListExp(self, nums: List[int], k: int) -> None:
        N = len(nums)
        k = k % N
        rotnums = [nums[(i-k)%N] for i in range(N)]
        for i in range(N):
            nums[i] = rotnums[i]

    def rotateO1(self, nums: List[int], k: int) -> None:
        """O(n) time O(1) space"""
        def rotate_inplace(l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        k %= len(nums)
        rotate_inplace(0, len(nums)-1)
        rotate_inplace(0, k-1)
        rotate_inplace(k, len(nums)-1)


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
        ([-1,-100,3,99], 2, [3,99,-1,-100]),
        ([1,2], 1, [2,1]),
        ([1,2], 2, [1,2]),
        ([1,2], 5, [2,1]),
        ([1,2,3,4,5], 3, [3,4,5,1,2,]),
        ([1,2,3], 3, [1,2,3]),
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

    def testCases_rotatePy(self):
        for nums, k, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                numsIn = [i for i in nums]
                # act
                s.rotatePy(numsIn, k)
                # assert
                self.assertEqual(expected, numsIn, (nums, k))
    
    def testCases_rotateListExp(self):
        for nums, k, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                numsIn = [i for i in nums]
                # act
                s.rotateListExp(numsIn, k)
                # assert
                self.assertEqual(expected, numsIn, (nums, k))

    def testCases_rotateO1(self):
        for nums, k, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                numsIn = [i for i in nums]
                # act
                s.rotateO1(numsIn, k)
                # assert
                self.assertEqual(expected, numsIn, (nums, k))

if __name__ == '__main__':
    unittest.main()
