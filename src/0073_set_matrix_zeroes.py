from typing import *
# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        O(m*n) time
        O(m+n) space
        """
        rows0 = set()  # x
        cols0 = set()  # y
        for x, row in enumerate(matrix):
            for y, c in enumerate(row):
                if c == 0:
                    rows0.add(x)
                    cols0.add(y)
        for row in rows0:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
        for col in cols0:
            for i in range(len(matrix)):
                matrix[i][col] = 0
            

from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = [
        ([], []),
        ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]),
        ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]),
    ]

    def testCases_setZeroes(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                numsCopy = [[i for i in n] for n in nums]
                # act
                s.setZeroes(nums)
                # assert
                self.assertEqual(expected, nums, (numsCopy))

if __name__ == '__main__':
    unittest.main()
