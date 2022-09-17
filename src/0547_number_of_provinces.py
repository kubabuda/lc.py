from typing import *
# https://leetcode.com/problems/number-of-provinces


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        neighbors = { i: set() for i in range(n) }
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    neighbors[i].add(j)
                    neighbors[j].add(i)
        
        visited = set()
        def dfs(node, prev=-1):
            if node in visited: return
            visited.add(node)
            for ne in neighbors[node]:
                if ne != prev and ne != node: dfs(ne, node)
        
        result = 0
        for i in range(n):
            if i not in visited:
                result += 1
                dfs(i)
        return result


from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    
    param_list = [
        ([], 0),
        ([[1,1,0],
          [1,1,0],
          [0,0,1]], 2),
        ([[1,0,0],
          [0,1,0],
          [0,0,1]], 3),
        ([[1,0,0,1],
          [0,1,1,0],
          [0,1,1,1],
          [1,0,1,1]], 1),
        ([[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],
          [0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
          [0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],
          [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
          [0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
          [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
          [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],
          [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
          [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]], 3)
    ]

    def testCases(self):
        for isConnected, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findCircleNum(isConnected)
                # assert
                self.assertEqual(expected, result, (isConnected))

if __name__ == '__main__':
    unittest.main()
