from typing import *
# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """O(log(n)) time O(1) space"""
        absdividend, absdivisor = abs(dividend), abs(divisor)
        if absdivisor > absdividend: return 0
        is_positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        quotient, mul = 0, 1
        
        while absdividend >= absdivisor:
            while absdividend >= absdivisor:
                absdividend -= absdivisor
                quotient += mul
                mul += mul
                absdivisor += absdivisor
            absdivisor = abs(divisor)
            mul = 1
        
        if not is_positive:
            quotient = -quotient
        return min(max(-2147483648, quotient), 2147483647)


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        (7, -3, -2),
        (10, 3, 3),
        (1, 2, 0),
        (-2147483648, -1, 2147483647),
    ]

    def testCases_divide(self):
        for dividend, divisor, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.divide(dividend, divisor)
                # assert
                self.assertEqual(expected, result, (dividend, divisor))


if __name__ == '__main__':
    unittest.main()
