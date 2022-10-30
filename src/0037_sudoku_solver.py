from typing import *
# 37. Sudoku Solver
# https://leetcode.com/problems/sudoku_solver

class Solution:
    def isValidSudoku(self, board: List[List[int]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [[set() for col in range(3)] for row in range(3)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.': continue
                
                if val in rows[row]: return False
                rows[row].add(val)
                
                if val in cols[col]: return False
                cols[col].add(val)

                brow, bcol = int(row/3), int(col/3)             
                if val in boxes[brow][bcol]:
                    return False
                boxes[brow][bcol].add(val)
        return True


import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        ([["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]], True            
        ),
        ([["8","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]], False
        ),
    ]

    def testCases_isValidSudoku(self):
        for board, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.isValidSudoku(board)
                # assert
                self.assertEqual(expected, result, (board))

if __name__ == '__main__':
    unittest.main()
