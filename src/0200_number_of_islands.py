from typing import *
import collections
# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''recursive DFS'''
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

    def numIslands2(self, grid: List[List[str]]) -> int:
        '''iterative BFS'''
        visited = set()
        islands = 0
        max_r = len(grid)
        max_c = len(grid[0])
        
        def bfs(rc):
            to_visit = collections.deque()
            to_visit.append(rc)

            while(to_visit):
                rc = to_visit.popleft()
                r,c = rc
                if not rc in visited and grid[r][c] != '0':
                    if r > 0: to_visit.append((r - 1, c))
                    if c > 0: to_visit.append((r, c - 1))
                    if r + 1 < max_r: to_visit.append((r + 1, c))
                    if c + 1<  max_c: to_visit.append((r, c + 1))
                    visited.add(rc)
        
        for r in range(max_r):
            for c in range(max_c):
                if grid[r][c] != '0':
                    rc = (r,c) 
                    if rc not in visited:
                        bfs(rc)
                        islands += 1
        return islands

    def numIslands3(self, grid: List[List[str]]) -> int:
        '''iterative DFS'''
        visited = set()
        islands = 0
        max_r = len(grid)
        max_c = len(grid[0])
        
        def bfs(rc):
            to_visit = collections.deque()
            to_visit.append(rc)

            while(to_visit):
                rc = to_visit.pop()
                r,c = rc
                if not rc in visited and grid[r][c] != '0':
                    if r > 0: to_visit.append((r - 1, c))
                    if c > 0: to_visit.append((r, c - 1))
                    if r + 1 < max_r: to_visit.append((r + 1, c))
                    if c + 1<  max_c: to_visit.append((r, c + 1))
                    visited.add(rc)
        
        for r in range(max_r):
            for c in range(max_c):
                if grid[r][c] != '0':
                    rc = (r,c) 
                    if rc not in visited:
                        bfs(rc)
                        islands += 1
        return islands


import unittest
class SolutionTests(unittest.TestCase): 
    param_list = param_list = [
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
            ["1","1","0","0","0"],
            ["0","0","0","0","0"],
            ["0","0","0","1","1"]
        ], 2),
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

    def testCases(self):
        for grid, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.numIslands(grid)
                # assert
                self.assertEqual(expected, result, (grid))
    
    def testCases2(self):
        for grid, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.numIslands2(grid)
                # assert
                self.assertEqual(expected, result, (grid))

    def testCases3(self):
        for grid, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.numIslands3(grid)
                # assert
                self.assertEqual(expected, result, (grid))

if __name__ == '__main__':
    unittest.main()
