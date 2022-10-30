from typing import *
# 37. Sudoku Solver
# https://leetcode.com/problems/sudoku_solver

class Solution:
    def solveSudoku(self, board: List[List[int]]) -> None:
        """"Computerphile algo with backtrack"""
        def isPossible(row, col, val) -> bool:
            for i in range(9):
                if board[row][i] == val: return False
                if board[i][col] == val: return False
            grrow, grcol = (row // 3) * 3, (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[grrow+i][grcol+j] == val: 
                        return False
            return True
        
        values = ['1','2','3','4','5','6','7','8','9']
        empty = '.'
        solved = False

        def solve(board):
            nonlocal solved
            for row in range(9):
                for col in range(9):
                    if board[row][col] == empty:
                        if solved: break
                        for value in values:
                            if not solved and isPossible(row, col, value):
                                board[row][col] = value
                                solve(board)
                                if not solved: 
                                    board[row][col] = empty # backtrack
                        return
            solved = True

        solve(board)


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
          [".",".",".",".","8",".",".","7","9"]],
         [["5","3","4","6","7","8","9","1","2"],
          ["6","7","2","1","9","5","3","4","8"],
          ["1","9","8","3","4","2","5","6","7"],
          ["8","5","9","7","6","1","4","2","3"],
          ["4","2","6","8","5","3","7","9","1"],
          ["7","1","3","9","2","4","8","5","6"],
          ["9","6","1","5","3","7","2","8","4"],
          ["2","8","7","4","1","9","6","3","5"],
          ["3","4","5","2","8","6","1","7","9"]]      
        ),
    ]

    def testCases_solveSudoku(self):
        for board, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                sol.solveSudoku(board)
                # assert
                self.assertEqual(expected, board)

if __name__ == '__main__':
    unittest.main()
