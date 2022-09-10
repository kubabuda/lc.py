from typing import *
# https://leetcode.com/problems/number-of-1-bits
import math
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        bits = 32
        for i in range(bits):
            result <<= 1
            mask = 1 << i
            if n & mask:
                result |= 1
        return result
        

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    def testCases(self):
        param_list = [
            (0b00000010100101000001111010011100, 0b00111001011110000010100101000000),
            (0b00000010100101000001111010011100, 964176192),
            (0b11111111111111111111111111111101, 3221225471),
        ]
        for n, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.reverseBits(n)
                # assert
                self.assertEqual(expected, result, (f'{n:b} gave {result:b} expected {expected:b}'))

if __name__ == '__main__':
    unittest.main()
