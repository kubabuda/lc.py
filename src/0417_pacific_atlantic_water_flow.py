from typing import *
# https://leetcode.com/problems/pacific-atlantic-water-flow
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visted = set()
        max_x = len(heights)
        max_y = len(heights[0])

        def dfs(x: int, y:int, solution, endfunc):
            xy = (x,y)
            if xy in solution: return True
            if xy in visted and xy not in solution: return False
            visted.add(xy)
            if endfunc(x,y):
                solution.add(xy)
                return True
            neighbors = []
            if x > 0: neighbors.append((x-1, y))
            if y > 0: neighbors.append((x, y-1))
            if x + 1 < max_x: neighbors.append((x+1,y))
            if y + 1 < max_y: neighbors.append((x,y+1))

            for ne in neighbors:
                ne_x, ne_y = ne
                if heights[ne_x][ne_y] <= heights[x][y]:
                    if ne in solution or dfs(ne_x, ne_y, solution, endfunc):
                        solution.add(xy)
                        return True
            return False

        # check Pacific starting from left upper corner surrounded by it
        toPacific = set()
        for x in range(max_x):
            for y in range(max_y):
                dfs(x, y, toPacific, lambda x,y: x == 0 or y == 0)
                visted.clear()
        # check Atlantic starting from right lower corner surrounded by it
        toAtlantic = set()
        last_x = max_x - 1
        last_y = max_y - 1
        for x in range(max_x):
            for y in range(max_y):
                dfs(last_x - x, last_y - y, toAtlantic, lambda x,y: x == last_x or y == last_y)
                visted.clear()
        # check points in both places
        result = []
        for xy in toAtlantic:
            if xy in toPacific:
                    result.append([xy[0],xy[1]])
        return result

    def pacificAtlantic2(self, heights: List[List[int]]) -> List[List[int]]:
        max_x = len(heights)
        max_y = len(heights[0])

        def dfs(x,y,solution,prevH):
            xy = (x,y)
            if xy in solution: return
            if heights[x][y] >= prevH:
                solution.add(xy)
                if x > 0: dfs(x-1, y, solution, heights[x][y])
                if y > 0: dfs(x, y-1, solution, heights[x][y])
                if x + 1 < max_x: dfs(x + 1, y, solution, heights[x][y])
                if y + 1 < max_y : dfs(x, y + 1, solution, heights[x][y])

        toAtlantic = set()
        toPacific = set()
        oceanH = -1
        last_x = max_x - 1
        last_y = max_y - 1
        
        for y in range(max_y):
            dfs(0, y, toPacific, oceanH)
            dfs(last_x, y, toAtlantic, oceanH)

        for x in range(max_x):
            dfs(x, 0, toPacific, oceanH)
            dfs(x, last_y, toAtlantic, oceanH)

        result = []
        for xy in toAtlantic: 
            if xy in toPacific:
                result.append([xy[0], xy[1]])
        return result

from unittest import TestCase
import unittest
class TestTemplate(unittest.TestCase): 

    param_list = lambda self: [
        ([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]], [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),
        ([[1]], [[0,0]]),
        ([[12,7,7,14,6,17,12,17,8,18,9,5],
            [6,8,12,5,3,6,2,14,19,6,18,13],
            [0,6,3,8,8,10,8,17,13,13,13,12],
            [5,6,8,8,15,16,19,14,7,11,2,3],
            [7,18,2,7,10,10,3,14,13,15,15,7],
            [18,6,19,4,12,3,3,2,6,6,19,6],
            [3,18,5,16,19,6,3,12,6,0,14,11],
            [9,10,17,12,10,11,11,9,0,0,12,0],
            [4,13,3,0,4,12,9,5,6,17,10,11],
            [18,3,5,0,8,19,18,4,8,19,1,3],
            [16,2,14,6,4,14,7,2,9,7,13,18],
            [0,16,19,16,16,4,15,19,7,0,3,16],
            [13,8,12,8,2,3,5,18,6,15,18,6],
            [4,10,8,1,16,0,6,0,14,10,11,8],
            [7,1,3,4,11,12,9,0,6,2,17,5],
            [1,16,6,1,0,19,11,1,5,7,8,2],
            [4,1,14,13,14,7,3,7,1,9,15,18],
            [14,11,6,14,14,14,4,0,11,17,1,9],
            [3,14,2,10,3,1,9,16,1,13,0,15],
            [8,9,13,5,5,7,10,1,4,5,0,9],
            [13,16,15,5,17,6,16,13,5,7,3,15],
            [5,1,12,19,3,13,0,0,3,10,6,13],
            [12,17,9,16,16,6,2,6,12,15,14,16],
            [7,7,0,6,4,15,1,7,17,5,2,12],
            [3,17,0,2,4,5,11,7,16,16,16,13],
            [3,7,16,11,2,16,14,9,16,17,10,3],
            [12,18,17,17,5,15,1,2,12,12,5,7],
            [11,10,10,0,11,7,17,14,5,15,2,16],
            [7,19,14,7,6,2,4,16,11,19,14,14],
            [6,17,6,6,6,15,9,12,8,13,1,7],
            [16,3,15,0,18,17,0,11,3,16,11,12],
            [15,12,4,6,19,15,17,7,3,9,2,11]],
            
            [[0,9],[0,10],[0,11],[1,8],[1,10],[1,11],[30,0],[31,0]]),
    ]

    def testCases(self):
        for heights, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.pacificAtlantic(heights)
                # assert
                expected = sorted(expected)
                result = sorted(result)
                self.assertEqual(expected, result, (heights))

    def testCases2(self):
        for heights, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.pacificAtlantic2(heights)
                # assert
                expected = sorted(expected)
                result = sorted(result)
                self.assertEqual(expected, result, (heights))

if __name__ == '__main__':
    unittest.main()