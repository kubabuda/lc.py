from typing import *
import collections
import heapq
# https://leetcode.com/problems/network-delay-time

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra algo
        edges = { i: [] for i in range(1, n + 1) }
        for e, v, weight in times:
            edges[e].append((v, weight))

        minheap = [(0, k)]
        visited = set()
        t = 0
        while minheap:
            weight, v = heapq.heappop(minheap)
            if v in visited: continue
            visited.add(v)
            t = max(t, weight)
            if v not in edges: continue
            for nv, nweight in edges[v]:
                heapq.heappush(minheap, (nweight + weight, nv))

        if len(visited) < n: return -1
        return t

from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = [
        ([[2,1,1],[2,3,1],[3,4,1]], 4, 2, 2),
        ([[1,2,1]], 2, 1, 1),
        ([[1,2,1]], 2, 2, -1),
        ([[1,2,1],[2,1,3]], 2, 2, 3),
        ([[1,2,1],[2,3,7],[1,3,4],[2,1,2]], 4, 4, -1),
    ]

    def testCases_networkDelayTime(self):
        for times, n, k, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.networkDelayTime(times, n, k)
                # assert
                self.assertEqual(expected, result, (times, n, k))

if __name__ == '__main__':
    unittest.main()
