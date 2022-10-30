from typing import *
# https://leetcode.com/problems/redundant-connection

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(max(i,j) for i,j in edges)
        nodes = { i: set() for i in range(1, n + 1)}
        for i,j in edges:
            nodes[i].add(j)
            nodes[j].add(i)
        visited = set()
        
        def dfs_isCycle(n, parent=-1):
            if n in visited:
                return True
            visited.add(n)
            for ne in nodes[n]:
                if ne != parent and dfs_isCycle(ne, n): return True
            return False

        for edge in edges[::-1]:
            i,j = edge
            nodes[i].remove(j)
            nodes[j].remove(i)
            visited.clear()
            if not dfs_isCycle(1) and len(visited) == n:
                return edge
            # backtrack
            nodes[i].add(j)
            nodes[j].add(i)
    
    def findRedundantConnectionUnionFind(self, edges: List[List[int]]) -> List[int]:
        n = max(max(i,j) for i,j in edges)
        pre = [i for i in range(n + 1)]
        rank = [1 for i in range(n + 1)]

        def find(n) -> int:
            p = pre[n]
            while pre[p] != p:
                pre[p] = pre[pre[p]]
                p = pre[p]
            return p

        def union(n1, n2) -> bool:
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return False

            if rank[p1] > rank[p2]:
                pre[p2] = p1
                rank[p1] += rank[p2]
            else:
                pre[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2): return [n1, n2]



import unittest

class SolutionTests(unittest.TestCase): 

    param_list = [
        ([[1,2],[1,3],[2,3]], [2,3]),
        ([[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4]),
        ([[3,4],[1,2],[2,4],[3,5],[2,5]], [2,5]),
    ]

    def testCases_findRedundantConnection(self):
        for edges, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findRedundantConnection(edges)
                # assert
                self.assertEqual(expected, result, (edges))

    def testCases_findRedundantConnectionUnionFind(self):
        for edges, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findRedundantConnectionUnionFind(edges)
                # assert
                self.assertEqual(expected, result, (edges))

if __name__ == '__main__':
    unittest.main()
