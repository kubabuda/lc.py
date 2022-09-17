from typing import *
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

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

    def testCases(self):
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
