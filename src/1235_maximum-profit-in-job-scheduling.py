from typing import *
# 1235. Maximum Profit in Job Scheduling
# https://leetcode.com/problems/maximum-profit-in-job-scheduling

class Solution:
    # bottom-up DP: O(N**2) time, O(N) memory. TLE
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit))
        
        PR = [j[2] for j in jobs]
        for i in range(N - 2, -1, -1):
            for j in range(i, N):
                if jobs[j][0] >= jobs[i][1]:
                    PR[i] = max(PR[i], PR[j] + jobs[i][2])
        return max(PR)

    # DFS: O(N**2) time, O(N) memory. TLE
    def jobScheduling_DFS(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(N)]
        jobs.sort(key=lambda x: x[0])
        
        cache = {}
        
        def dfs(i: int) -> int:
            job = jobs[i]
            p = job[2]
            for j in range(i + 1, N):
                nextJob = jobs[j]
                if nextJob[0] >= job[1]:
                    pj = cache[j] if j in cache else dfs(j)
                    p = max(p, job[2] + pj)
            cache[i] = p
            return p

        return max(dfs(j) for j in range(N))
    
    
import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ([1,2,3,3], [3,4,5,6], [50,10,40,70], 120),
        ([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60], 150),
        ([1,1,1], [2,3,4], [5,6,4], 6),
    ]

    def testCases_jobScheduling(self):
        for start, end, profit, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.jobScheduling(start, end, profit)
                # assert
                self.assertEqual(expected, result, (start, end, profit))

    def testCases_jobScheduling_DFS(self):
        for start, end, profit, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.jobScheduling_DFS(start, end, profit)
                # assert
                self.assertEqual(expected, result, (start, end, profit))

if __name__ == '__main__':
    unittest.main()
