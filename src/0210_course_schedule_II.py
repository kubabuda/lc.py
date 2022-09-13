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
                    curr = toVisit.pop()
                    if curr in visited and curr not in solutionSet:
                        return []
                    visited.add(curr)
                    pres = [pre for pre in coursePre[curr] if pre not in solutionSet]
                    if pres and any(pres):
                        toVisit.append(curr)
                        for pre in pres:
                            toVisit.append(pre)
                    else:
                        solutionList.append(curr)
                        solutionSet.add(curr)
                        coursePre[curr] = []

        return solutionList
        
from unittest import TestCase
import unittest
class TestTemplate(unittest.TestCase): 

    def testCases(self):
        param_list = [
            (2, [], [[0,1],[1,0]]),
            (2, [[0,1],[1,0]], [[]]),
            (2, [[1,0]], [[0,1]]),
            (2, [[0,1]], [[1,0]]),
            (4, [[1,0],[2,0],[3,1],[3,2]], [[0,2,1,3],[0, 1, 2, 3]]),
            (3, [[0,1],[1,2],[2,0]], [[]]),
        ]
        for numCourses, nodes, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findOrder(numCourses, nodes)
                # assert
                self.assertTrue(result in expected, (f'{numCourses} {nodes} returned {result} expected {expected}' ))

    def testCasesIter(self):
        param_list = [
            (2, [], [[0,1],[1,0]]),
            (2, [[0,1],[1,0]], [[]]),
            (2, [[1,0]], [[0,1]]),
            (2, [[0,1]], [[1,0]]),
            (4, [[1,0],[2,0],[3,1],[3,2]], [[0,2,1,3],[0, 1, 2, 3]]),
            (3, [[0,1],[1,2],[2,0]], [[]]),
        ]
        for numCourses, nodes, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findOrderIterative(numCourses, nodes)
                # assert
                self.assertTrue(result in expected, (f'{numCourses} {nodes} returned {result} expected {expected}' ))

if __name__ == '__main__':
    unittest.main()
