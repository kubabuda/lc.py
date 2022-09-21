from typing import *
# https://leetcode.com/problems/swim-in-rising-water
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        minheap = [(grid[0][0], 0, 0)] # (height, x, y)
        while minheap:
            maxH, x, y = heapq.heappop(minheap)
            if (x,y) in visited: continue
            visited.add((x,y))
            if x == y == n-1:
                return maxH
            if x > 0 and (x-1,y) not in visited: 
                heapq.heappush(minheap, (max(maxH, grid[x-1][y]), x-1,y))
            if y > 0 and (x,y-1) not in visited: 
                heapq.heappush(minheap, (max(maxH, grid[x][y-1]), x,y-1))
            if x + 1 < n and (x+1,y) not in visited: 
                heapq.heappush(minheap, (max(maxH, grid[x+1][y]), x+1,y))
            if y + 1 < n and (x,y+1) not in visited: 
                heapq.heappush(minheap, (max(maxH, grid[x][y+1]), x,y+1))


from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    
    param_list = [
        # ([0], 0),
        ([[0,2],
          [1,3]], 3),
        ([[3,2],
          [0,1]], 3),
        ([[0, 1, 2, 3, 4 ],
          [24,23,22,21,5 ],
          [12,13,14,15,16],
          [11,17,18,19,20],
          [10, 9, 8, 7, 6]], 16),
    ]

    def testCases_swimInWater(self):
        for grid, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.swimInWater(grid)
                # assert
                self.assertEqual(expected, result, (grid))

if __name__ == '__main__':
    unittest.main()
