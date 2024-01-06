from typing import *

# 2125. Number of Laser Beams in a Bank
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank

class Solution:
    '''O(N) time O(1) space'''
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prev = 0
        for row in bank:
            curr = 0
            for c in row:
                if c == '1':
                    curr += 1
            if curr:
                result += prev * curr
                prev = curr
        return result


import unittest

class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        (["011001","000000","010100","001000"], 8),
        (["000","111","000"], 0)
    ]

    def testCases_numberOfBeams(self):
        for bank, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.numberOfBeams(bank)
                # assert
                self.assertEqual(expected, result, (bank))

if __name__ == '__main__':
    unittest.main()
