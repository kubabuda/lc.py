from typing import *
# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        INT32_MAX = (2 ** 31) - 1
        result = 0
        X = abs(x)
        while X > 0:
            result *= 10
            result += X % 10
            X //= 10
            print(X, result)

        if result >= INT32_MAX:
            return 0
        if x < 0:
            return -result
        return result

import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda _: [
        (123, 321),
        (-123, -321),
        (0, 0),
    ]

    def testCases_reverse(self):
        for x, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.reverse(x)
                # assert
                self.assertEqual(result, expected, f'{x}: {result} != {expected}')


if __name__ == '__main__':
    unittest.main()
