from typing import *
# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix) - 1
        h = int(N / 2)
        hx = h + 1 if N % 2 else h

        for xi in range(hx):
            for yi in range(h + 1):
                temp = matrix[xi][yi]                       # LT
                matrix[xi][yi] = matrix[N - yi][xi]         # LL into LT
                matrix[N - yi][xi] = matrix[N - xi][N - yi] # RL into LL
                matrix[N - xi][N - yi] = matrix[yi][N - xi] # RT into RL
                matrix[yi][N - xi] = temp                   # LR into RT
        

from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
        ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]),
    ]

    def testCases_rotate(self):
        for matrix, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                cpy = [[c for c in r] for r in matrix]
                s.rotate(matrix)
                # assert
                self.assertEqual(expected, matrix, (cpy))

if __name__ == '__main__':
    unittest.main()
