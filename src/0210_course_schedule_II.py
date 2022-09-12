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
        
        
from unittest import TestCase
import unittest
class TestTemplate(unittest.TestCase): 

    def testCases(self):
        param_list = [
            (2, [], [[0,1],[1,0]]),
            (2, [[1,0]], [[0,1]]),
            (4, [[1,0],[2,0],[3,1],[3,2]], [[0,2,1,3],[0, 1, 2, 3]])
        ]
        for numCourses, nodes, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.findOrder(numCourses, nodes)
                # assert
                self.assertTrue(result in expected, (numCourses, nodes))

if __name__ == '__main__':
    unittest.main()
