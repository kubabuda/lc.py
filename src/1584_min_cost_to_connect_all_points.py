from typing import *
# https://leetcode.com/problems/min-cost-to-connect-all-points

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Kruskal algo"""
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

        mst = set() # minimal spanning tree
        cost_sum = 0
        for cost, p1, p2 in all_edges:
            if find(p1) != find(p2):
                union(p1, p2)
                mst.add((p1,p2))
                cost_sum += cost
        print(cost_sum, mst)
        return cost_sum

    def minCostConnectPoints2(self, points: List[List[int]]) -> int:
     
        def manhattan_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        def find(idx):
            while roots[idx] != idx:
                idx = roots[idx]
            return idx
        
        def union(p1, p2):
            x, y = find(p1), find(p2)
            if x != y:
                if ranks[x] >= ranks[y]:
                    roots[y] = x
                    ranks[x] += ranks[y]
                else:
                    roots[x] = y
                    ranks[y] += ranks[x]

        # generate MST
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1 = points[i]
                p2 = points[j]
                edges.append(
                    [i, j, manhattan_dist(p1, p2)]
                )
        edges = sorted(edges, key=lambda x: x[2])
        roots = [i for i in range(len(points))]
        ranks = [1 for i in range(len(points))]
        total_cost = 0
        
        for _from, _to, cost in edges:
            x = find(_from)
            y = find(_to)
            if x != y:
                if ranks[x] >= ranks[y]:
                    roots[y] = x
                    ranks[x] += ranks[y]
                else:
                    roots[x] = y
                    ranks[y] += ranks[x]

                total_cost += cost

        return total_cost

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    
    param_list = [
        ([[0,0],[2,2],[3,10],[5,2],[7,0]], 20),
        ([[3,12],[-2,5],[-4,1]], 18),
        ([[0,0],[1,1],[1,0],[-1,1]], 4),
    ]

    # def testCases_minCostConnectPoints(self):
    #     for points, expected in self.param_list:
    #         with self.subTest():
    #             # arrange
    #             s = Solution()
    #             # act
    #             result = s.minCostConnectPoints(points)
    #             # assert
    #             self.assertEqual(expected, result, (points))

    def testCases_minCostConnectPoints2(self):
        for points, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.minCostConnectPoints2(points)
                # assert
                self.assertEqual(expected, result, (points))

if __name__ == '__main__':
    unittest.main()
