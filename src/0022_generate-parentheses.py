from typing import *
# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses

class Solution:
    """https://leetcode.com/problems/generate-parentheses/solutions/2542620/python-java-w-explanation-faster-than-96-w-proof-easy-to-understand"""
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(l, r, s):
            if len(s) == n * 2:
                result.append(s)
                return
            if l < n:
                dfs(l + 1, r, s + '(')
            if r < l:
                dfs(l, r + 1, s + ')')
        
        dfs(0, 0, '')
        return result


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        (1, ["()"]),
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
        (4, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]),
    ]

    def testCases_generateParenthesis(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.generateParenthesis(nums)
                # assertg
                self.assertEqual(sorted(expected), sorted(result), (nums))


if __name__ == '__main__':
    unittest.main()
