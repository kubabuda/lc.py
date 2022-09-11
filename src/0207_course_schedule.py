from typing import *
# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = { i: [] for i in range(0, numCourses) } # course: [precedingCourse]
        for p in prerequisites:
            nodes[p[0]].append(p[1])
        for course in range(0, numCourses):
            visited = set()
            to_visit = [course]
            while to_visit:
                curr = to_visit.pop()
                visited.add(curr)
                for pre in nodes[curr]:
                    if pre == course:
                        return False
                    if pre not in visited:
                        to_visit.append(pre)
        return True

from unittest import TestCase
import unittest
class TestTemplate(unittest.TestCase): 
    def testCases(self):
        param_list = [
            # (2, [], True),
            # (2, [[1,0]], True),
            (2, [[1,0],[0,1]], False),
            # (5, [[1,4],[2,4],[3,1],[3,2]], True)
        ]
        for numCourses, nodes, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.canFinish(numCourses, nodes)
                # assert
                self.assertEqual(expected, result, (numCourses, nodes))

if __name__ == '__main__':
    unittest.main()
