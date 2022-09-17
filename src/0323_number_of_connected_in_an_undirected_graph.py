from typing import *
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = { i: set() for i in range(n) }
        for i,j in edges:
            nodes[i].add(j)
            nodes[j].add(i)
        visited = set()
        
        def visit_dfs(node):
            if node in visited: return
            visited.add(node)
            for ne in nodes[node]:
                visit_dfs(ne)

        result = 0
        for node in range(n):
            if node not in visited:
                result += 1
                visit_dfs(node)
        return result

    def countComponents_unionFind(self, n: int, edges: List[List[int]]) -> int:
        if n == 0 or not edges: return n
        parent = [i for i in range(n)]

        for i,j in edges:
            i_root = parent[i]
            while i_root != parent[i_root]:
                i_root = parent[i_root]
            parent[i] = i_root
            parent[j] = i_root

        result = set()
        for i in parent:
            if i not in result:
                result.add(i)

        return len(result)

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    
    param_list = [
        (0, [], 0),
        (2, [], 2),
        (5, [[0,1],[0,2],[0,3],[1,4]], 1),
        (5, [[0, 1], [1, 2], [3, 4]], 2),
        (6, [[0,1],[0,2],[0,3],[1,4]], 2),
        (4, [[3, 2], [2, 1], [3, 0]], 1),
        # (15, [[13, 8], [10, 5], [11, 10], [8, 7], [10, 4], [5, 3], [7, 0], [11, 9], [14, 9], [13, 6], [8, 6], [1, 0], [6, 3], [9, 4]], 3),
        (15, [(0, 1), (0, 7), (4, 10), (10, 11), (4, 9), (6, 8), (8, 13), (5, 10), (6, 13), (7, 8), (3, 6), (9, 14), (9, 11), (3, 5)], 3)
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

    def testCases_unionFind(self):
        for n, edges, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.countComponents_unionFind(n, edges)
                # assert
                self.assertEqual(expected, result, (n, edges))

if __name__ == '__main__':
    unittest.main()
