from typing import *
# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        max_r = len(grid)
        max_c = len(grid[0])
        
        def dfs(r,c) -> bool:
            if grid[r][c] == '0' or (r,c) in visited: return False
            visited.add((r,c))
            if r > 0: dfs(r - 1, c)
            if c > 0: dfs(r, c - 1)
            if r + 1 < max_r: dfs(r + 1, c)
            if c + 1<  max_c: dfs(r, c + 1)

            return True
        
        for r in range(max_r):
            for c in range(max_c):
                if dfs(r,c): islands += 1
        
        return islands

from unittest import TestCase
import unittest
class TestTemplate(unittest.TestCase): 

    def testCases(self):
        param_list = [
            ([
                ["0","0","0","0","0"],
                ["0","0","0","0","0"],
                ["0","0","0","0","0"],
                ["0","0","0","0","0"]
            ], 0),
            ([
                ["1","1","1","1","1"],
                ["1","1","1","1","1"],
                ["1","1","1","1","1"],
                ["1","1","1","1","1"]
            ], 1),
            ([
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ], 1),
            ([
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ], 3),
        ]
        for grid, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.numIslands(grid)
                # assert
                self.assertEqual(expected, result, (grid))

if __name__ == '__main__':
    unittest.main()
