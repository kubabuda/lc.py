from typing import *
# https://leetcode.com/problems/graph-valid-tree

class Solution:
    def isValidTree(self, n, edges: List[List[int]]) -> bool:
        if not n: return True
        node_neighbors = { i: set() for i in range(n) }
        for i,j in edges:
            node_neighbors[i].add(j)
            node_neighbors[j].add(i)
        visited = set()
        
        def dfs(node, parent = -1) -> bool:
            # print("NN", node, visited)
            if node in visited:
                # print("YYY", node, visited)
                return False
            visited.add(node)
            for ne in node_neighbors[node]:
                if ne != parent:
                    if not dfs(ne, node): return False
            return True
        if not dfs(0): return False
        if len(visited) < n: return False

        return True

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 

    param_list = [
        (0, [], True),
        (5, [[0,1],[0,2],[0,3],[1,4]], True),
        (6, [[0,1],[0,2],[0,3],[1,4]], False),
        (5, [[0,1],[0,2],[0,3],[1,4],[4,0]], False),
    ]

    def testCases(self):
        for n, edges, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.isValidTree(n, edges)
                # assert
                self.assertEqual(expected, result, (n, edges))

if __name__ == '__main__':
    unittest.main()
