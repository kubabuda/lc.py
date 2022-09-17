from typing import *
# https://leetcode.com/problems/

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = { i: set() for i in range(n) }
        for i,j in edges:
            nodes[i].add(j)
            nodes[j].add(i)
        visited = set()
        
        def visit_dfs(node, prev = -1):
            if node in visited: return False
            visited.add(node)
            for ne in nodes[node]:
                if ne != prev and not visit_dfs(ne, node): return False
            return True

        result = 0
        for node in range(n):
            if node not in visited:
                result += 1
                if not visit_dfs(node):
                    pass # cycle detected
        return result

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    
    param_list = [
        (0, [], 0),
        (5, [[0,1],[0,2],[0,3],[1,4]], 1),
        (5, [[0, 1], [1, 2], [3, 4]], 2),
        (6, [[0,1],[0,2],[0,3],[1,4]], 2),
    ]

    def testCases(self):
        for n, edges, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.countComponents(n, edges)
                # assert
                self.assertEqual(expected, result, (n, edges))

if __name__ == '__main__':
    unittest.main()
