from typing import *
# 79. Word Search
# https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        
        def isWord(x, y, i = 0):
            if board[x][y] != word[i]: return False
            if i + 1 >= len(word): return True
            board[x][y] = ' '
            nei = i + 1
            if x > 0 and isWord(x-1, y, nei) \
            or x+1 < M and isWord(x+1, y, nei) \
            or y > 0 and isWord(x, y-1, nei) \
            or y+1 < N and isWord(x, y+1, nei):
                return True
            board[x][y] = word[i]
            return False
    
        for x in range(M):
            for y in range(N):
                if isWord(x, y): return True
        return False


from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        ([['a']], 'a', True),
        ([['a']], 'b', False),
        ([["A","B","C","E"],
          ["S","F","C","S"],
          ["A","D","E","E"]], "ABCCED", True),
        ([["A","B","C","E"],
          ["S","F","C","S"],
          ["A","D","E","E"]],"SEE", True),
    ]

    def testCases_exist(self):
        for board, word, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.exist(board, word)
                # assert
                self.assertEqual(expected, result, (board, word))

if __name__ == '__main__':
    unittest.main()
