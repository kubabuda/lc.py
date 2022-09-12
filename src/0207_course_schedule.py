from typing import *
from collections import deque
# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # populate hashSet { course: [precedingCourse] }
        nodes = { i: [] for i in range(0, numCourses) }
        for course, prerequisite in prerequisites:
            nodes[course].append(prerequisite)
        # iterate over every course
        visited = set()
        to_visit = deque()
        for course in range(0, numCourses):
            to_visit.clear()
            to_visit.append(course)
            visited.clear()
            while to_visit:
                curr = to_visit.pop()
                visited.add(curr)
                for pre in nodes[curr]:
                    if pre == course:
                        return False
                    if pre not in visited:
                        to_visit.append(pre)
        return True

    def canFinishRec(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = { i: [] for i in range(0, numCourses) }
        for course, prerequisite in prerequisites:
            nodes[course].append(prerequisite)

        def canFinish(course, visited):
            if course in visited: 
                return False
            visited.add(course)
            for ne in nodes[course]:
                if not canFinish(ne, visited):
                    return False
            nodes[course].clear()
            return True

        for c in range(numCourses):
            visited = set()
            if nodes[c] and not canFinish(c, visited):
                return False
        return True


from unittest import TestCase
import unittest
class TestTemplate(unittest.TestCase): 

    def testCases(self):
        param_list = [
            (2, [], True),
            (2, [[1,0]], True),
            (2, [[1,0],[0,1]], False),
            (5, [[1,4],[2,4],[3,1],[3,2]], True),
            (4, [[0,1],[3,1],[1,3],[3,2]], False),
        ]
        for numCourses, nodes, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.canFinish(numCourses, nodes)
                # assert
                self.assertEqual(expected, result, (numCourses, nodes))

    def testCasesRec(self):
        param_list = [
            (2, [], True),
            (2, [[1,0]], True),
            (2, [[1,0],[0,1]], False),
            (5, [[1,4],[2,4],[3,1],[3,2]], True),
            (4, [[0,1],[3,1],[1,3],[3,2]], False),
        ]
        for numCourses, nodes, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.canFinishRec(numCourses, nodes)
                # assert
                self.assertEqual(expected, result, (numCourses, nodes))

if __name__ == '__main__':
    unittest.main()
