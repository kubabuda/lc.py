from typing import *
# https://leetcode.com/problems/min-cost-to-connect-all-points
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Kruskal algo"""

        def manhattan(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        def find(p) -> int:
            root = pre[p]
            while pre[root] != root:
                pre[root] = pre[pre[root]]
                root = pre[root]
            return root
        
        def union(v1, v2) -> bool:
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return False
            if ranks[p1] >= ranks[p1]:
                pre[p2] = p1
                ranks[p1] += ranks[p2]
            else:
                pre[p1] = p2
                ranks[p2] += ranks[p1]
            return True
        
        all_edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                all_edges.append((manhattan(i,j), i, j))
        all_edges.sort()

        pre = [ i for i in range(len(points)) ]
        ranks = [ 1 for p in pre ]

        # mst = set() # minimal spanning tree
        cost_sum = 0
        for cost, p1, p2 in all_edges:
            if find(p1) != find(p2):
                union(p1, p2)
                # mst.add((p1,p2))
                cost_sum += cost    
        return cost_sum
    
    def minCostConnectPointsPrim(self, points: List[List[int]]) -> int:
        """Prim algo"""
        def manhattan(i, j):
            p1, p2 = points[i], points[j]
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        visited = set()
        dist_sum = 0
        minheap = [(0,0)]

        while minheap:
            dist, node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            dist_sum += dist
            for i in range(len(points)):
                if i != node and not i in visited:
                    heapq.heappush(minheap, (manhattan(node, i), i))
        
        return dist_sum



import unittest

class SolutionTests(unittest.TestCase): 
    
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

    def testCases_minCostConnectPointsPrim(self):
        for points, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.minCostConnectPointsPrim(points)
                # assert
                self.assertEqual(expected, result, (points))

if __name__ == '__main__':
    unittest.main()
