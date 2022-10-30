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
        rows0 = set()
        cols0 = set()
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
    
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        O(m*n) time
        O(1) space
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        first = False
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row == 0:
                        first = True
                    else:
                        matrix[row][0] = 0
        for row in matrix[1:]:
            if row[0] == 0:
                for col in range(COLS):
                    row[col] = 0
        for col in range(COLS):
            if matrix[0][col] == 0:
                for row in range(ROWS):
                    matrix[row][col] = 0
        if first:
            for col in range(COLS):
                    matrix[0][col] = 0



import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda _: [
        ([[1,0]], [[0,0]]),
        ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]),
        ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]),
        ([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]], [[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        ([[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]], [[0,0,0,0,0],[0,0,0,0,0],[2147483647,2,-9,-6,0]]),
    ]

    def testCases_setZeroes(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                numsCopy = [[i for i in n] for n in nums]
                # act
                s.setZeroes(nums)
                # assert
                self.assertEqual(expected, nums, (numsCopy))

    def testCases_setZeroes2(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                numsCopy = [[i for i in n] for n in nums]
                # act
                s.setZeroes2(nums)
                # assert
                self.assertEqual(expected, nums, (numsCopy))

if __name__ == '__main__':
    unittest.main()
