from typing import *
# https://leetcode.com/problems/number-of-1-bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            if n & 1: result += 1
            n >>= 1
        return result
        


import unittest

class SolutionTests(unittest.TestCase): 
    def testCases(self):
        param_list = [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (0b00000000000000000000000000001011, 3),
            (0b00000000000000000000000010000000, 1),
            (0b11111111111111111111111111111101, 31),
        ]
        for n, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.hammingWeight(n)
                # assert
                self.assertEqual(expected, result, (n))

if __name__ == '__main__':
    unittest.main()
