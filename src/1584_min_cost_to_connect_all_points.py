from typing import *
# "title".toLocaleLowerCase().replaceAll(".","").replaceAll(" ", "_").replaceAll("-","_");
# https://leetcode.com/problems/min-cost-to-connect-all-points

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattanDist(p1, p2) -> int:
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1-x2) + abs(y1-y2)

        all_edges = []
        for i, p1 in enumerate(points):
            x1, y1 = p1
            p1 = (x1, y1)
            for x2, y2 in points[i+1:]:
                p2 = (x2, y2)
                if x1 != x2 and y1 != y2:
                    all_edges.append((manhattanDist(p1,p2), p1, p2))
        all_edges.sort()

        pre = { (x,y):(x,y) for x,y in points }
        rank = { p: 1 for p in pre }

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

        mst = set()
        cost_sum = 0
        for cost, p1, p2 in all_edges:
            if union(p1, p2):
                mst.add((p1,p2))
                cost_sum += cost
        # print(mst)
        
        return cost_sum

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    
    param_list = [
        ([[0,0],[2,2],[3,10],[5,2],[7,0]], 20),
        ([[3,12],[-2,5],[-4,1]], 18),
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
