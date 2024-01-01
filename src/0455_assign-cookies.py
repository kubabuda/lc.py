from typing import *
# 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies

class Solution:
    '''two sorted stacks: O(N) space O(N log N) time'''
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cookies = sorted(s, reverse=True)
        kids = sorted(g, reverse=True)
        result = 0
        while cookies and kids:
            while cookies and kids and cookies[-1] < kids[-1]:
                cookies.pop()
            if not cookies or not kids:
                break
            cookie = cookies.pop()
            if kids and kids[-1] <= cookie:
                kids.pop()
                result += 1
            
        return result


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ([1,2,3], [1,1], 1),
        ([1,2], [1,2,3], 2),
        ([1,2], [], 0),
        ([], [1,2,3], 0),
    ]

    def testCases_findContentChildren(self):
        for g, s, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.findContentChildren(g, s)
                # assertg
                self.assertEqual(expected, result, (g, s))


if __name__ == '__main__':
    unittest.main()
