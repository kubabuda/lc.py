from typing import *
# https://leetcode.com/problems/sum-of-two-integers/
class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = 0
        carry = 0
        n_bit = 0
        bit_a = 0
        bit_b = 0
        BITS = 32
        for i in range(0, BITS):
            bit_a = a & 1
            bit_b = b & 1
            a >>= 1
            b >>= 1
            if carry and bit_a and bit_b:
                n_bit = 1
            elif (bit_a and bit_b) or (bit_a and carry) or (bit_b and carry):
                carry = 1
                n_bit = 0
            elif bit_a or bit_b or carry:
                n_bit = 1
                carry = 0
            else:
                n_bit = 0
                carry = 0
            n_bit <<= BITS
            result |= n_bit
            result >>= 1

        return result
        

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    def testCases(self):
        param_list = [
            (1,2, 3),
            (1,1, 2),
            (2,3, 5),
            (0,1, 1),
        ]
        for a, b, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.getSum(a, b)
                # assert
                self.assertEqual(expected, result, (a, b))

if __name__ == '__main__':
    unittest.main()
