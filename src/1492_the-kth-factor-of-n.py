from typing import *
from math import ceil, sqrt
# 1492. The kth Factor of n
# https://leetcode.com/problems/the-kth-factor-of-n

class Solution:
    '''greedy: N space N time'''
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range (1, (n // 2) + 1):
            if n // i == n / i:
                factors.append(i)
        factors.append(n)

        if len(factors) < k:
            return -1
        return factors[k - 1]

import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        (12, 3, 3),
        (12, 4, 4),
        (12, 5, 6),
        (12, 6, 12),
        (7, 2, 7),
        (4, 4, -1),
        (1, 1, 1),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 2),
        (9, 2, 3),
        (420, 25, -1),
        (702, 11, 54)
    ]

    def testCases_kthFactor(self):
        for n, k, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.kthFactor(n, k)
                # assert
                self.assertEqual(expected, result, (n, k))


if __name__ == '__main__':
    unittest.main()
