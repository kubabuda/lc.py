from typing import *
# 79. Word Search
# https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        
        def isWord(word, point, visited = None):
            if not word: return True
            x,y = point
            if board[x][y] != word[0]: return False
            if not visited: visited = set()
            if point in visited: return False
            visited.add(point)
            wordRem = word[1:]
            if not wordRem: return True
            nei = []
            if x > 0: nei.append((x-1, y))
            if x+1 < M: nei.append((x+1, y))
            if y > 0: nei.append((x, y-1))
            if y+1 < N: nei.append((x, y+1))
            pos_nei = [(m,n) for m,n in nei if (m,n) not in visited]
            for ne in pos_nei:
                if isWord(wordRem, ne, visited): return True
            visited.remove(point)
            return False
    
        for x in range(M):
            for y in range(N):
                if isWord(word, (x,y)): return True
        return False    


from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        ([['a']], 'a', True),
        ([['a']], 'b', False),
        # ([["A","B","C","E"],
        #   ["S","F","C","S"],
        #   ["A","D","E","E"]], "ABCCED", True),
        # ([["A","B","C","E"],
        #   ["S","F","C","S"],
        #   ["A","D","E","E"]],"SEE", True),
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
