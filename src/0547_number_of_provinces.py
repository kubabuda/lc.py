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

    def findCircleNum_unionFind(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        pre = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(n):
            p = n
            while p != pre[p]:
                pre[p] = pre[pre[p]]
                p = pre[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return 0
            
            if rank[p1] > rank[p2]:
                pre[p2] = p1
                rank[p1] += rank[p2]
            else:
                pre[p1] = p2
                rank[p2] = p1
            return 1

        result = n
        for i in range(n):
            for j in range(0, i):
                if isConnected[j][i] and i != j:
                    result -= union(i, j)
        return result


import unittest

class SolutionTests(unittest.TestCase): 
    
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

    def testCases_unionFind(self):
        for isConnected, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findCircleNum_unionFind(isConnected)
                # assert
                self.assertEqual(expected, result, (isConnected))

if __name__ == '__main__':
    unittest.main()
