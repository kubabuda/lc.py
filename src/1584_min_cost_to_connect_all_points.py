from typing import *
# "title".toLocaleLowerCase().replaceAll(".","").replaceAll(" ", "_").replaceAll("-","_");
# https://leetcode.com/problems/min-cost-to-connect-all-points

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        all_edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                all_edges.append((dist, i, j))
        all_edges.sort()

        pre = [ i for i in range(len(points)) ]
        rank = [ p for p in pre ]

        def find(p) -> int:
            root = pre[p]
            while pre[root] != root:
                pre[root] = pre[pre[root]]
                root = pre[root]
            return root
        
        def union(p1, p2) -> bool:
            pre1, pre2 = find(p1), find(p2)
            if pre1 == pre2:
                return False
            if rank[p1] >= rank[p1]:
                pre[p2] = p1
                rank[p1] += rank[p2]
            else:
                pre[p1] = p2
                rank[p2] += rank[p1]
            return True

        # mst = set() # minimal spanning tree
        cost_sum = 0
        for cost, p1, p2 in all_edges:
            if find(p1) != find(p2):
                union(p1, p2)
                # mst.add((p1,p2))
                cost_sum += cost
        
        return cost_sum

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    
    param_list = [
        ([[0,0],[2,2],[3,10],[5,2],[7,0]], 20),
        ([[3,12],[-2,5],[-4,1]], 18),
        ([[0,0],[1,1],[1,0],[-1,1]], 4),
    ]

    def testCases_minCostConnectPoints(self):
        for points, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.minCostConnectPoints(points)
                # assert
                self.assertEqual(expected, result, (points))

if __name__ == '__main__':
    unittest.main()
