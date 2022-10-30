from typing import *
from collections import deque
# https://leetcode.com/problems/course-schedule/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = { i: [] for i in range(numCourses) }
        for course, pre in prerequisites:
            courses[course].append(pre)
        solutionSet = set()
        solutionList = []
        
        def dfs(course, visited):
            if course in visited and course not in solutionSet:
                return False
            visited.add(course)
            for pre in courses[course]:
                if not dfs(pre, visited):
                    return False
            
            if course not in solutionSet:
                solutionSet.add(course)
                solutionList.append(course)
            return True        

        for course in courses:
            if course not in solutionSet:
                visited = set()
                if not dfs(course, visited):
                    return []
        
        return solutionList

    def findOrderIterative(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        coursePre = { i:[] for i in range(numCourses) }
        for c, pre in prerequisites:
            coursePre[c].append(pre)
        solutionSet = set()
        solutionList = []
        toVisit = deque()

        for course in coursePre:
            visited = set()
            if course not in solutionSet:
                toVisit.append(course)

                while toVisit:
                    curr = toVisit[-1]
                    if curr in visited and curr not in solutionList and curr != course:
                        return []
                    visited.add(curr)

                    pres = [pre for pre in coursePre[curr] if pre not in solutionSet]
                    if pres:
                        for pre in pres:
                            if pre in visited and pre not in solutionList:
                                return []
                            else:
                                toVisit.append(pre)
                    else:
                        toVisit.pop()
                        solutionList.append(curr)
                        solutionSet.add(curr)
                        coursePre[curr] = []

        return solutionList
        

import unittest
class SolutionTests(unittest.TestCase): 
    
    param_list = [
        (2, [], [[0,1],[1,0]]),
        (2, [[0,1],[1,0]], [[]]),
        (2, [[1,0]], [[0,1]]),
        (2, [[0,1]], [[1,0]]),
        (4, [[1,0],[2,0],[3,1],[3,2]], [[0,2,1,3],[0, 1, 2, 3]]),
        (3, [[0,1],[1,2],[2,0]], [[]]),
        (6, [[0,1],[0,2],[1,3],[3,2],[4,0],[5,0]], [[2,3,1,0,4,5],[2,3,1,0,4,5]]),
        (7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]], [[6,5,4,2,3,0,1]]),
    ]

    def testCases(self):
        for numCourses, nodes, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findOrder(numCourses, nodes)
                # assert
                self.assertTrue(result in expected, (f'{numCourses} {nodes} returned {result} expected {expected}' ))

    def testCasesIter(self):
        for numCourses, nodes, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findOrderIterative(numCourses, nodes)
                # assert
                self.assertTrue(result in expected, (f'{numCourses} {nodes} returned {result} expected {expected}' ))

if __name__ == '__main__':
    unittest.main()
