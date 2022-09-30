from typing import *
# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        xs, xe = 0, len(matrix) - 1
        ys, ye = 0, len(matrix[0]) - 1
        result = []
        while (xs < xe and ys <= ye) or (ys < ye and xs <= xe):
            for y in range(ys, ye + 1):
                result.append(matrix[xs][y])
            for x in range(xs + 1, xe):
                result.append(matrix[x][ye])
            if xs < xe:
                for y in reversed(range(ys, ye + 1)):
                    result.append(matrix[xe][y])
            if ys < ye:
                for x in reversed(range(xs + 1, xe)):
                    result.append(matrix[x][ys])
            xs += 1
            xe -= 1
            ys += 1
            ye -= 1
        if xs == xe == ys == ye:
            result.append(matrix[xs][ys])
        return result
        

from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        ([[1]], [1]),
        ([[1],[2],[3],[4]], [1,2,3,4]),
        ([[1,2,3,4]], [1,2,3,4]),
        ([[1,2],[3,4]], [1,2,4,3]),
        ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
    ]

    def testCases_spiralOrder(self):
        for matrix, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.spiralOrder(matrix)
                # assert
                self.assertEqual(expected, result, (matrix))

if __name__ == '__main__':
    unittest.main()
