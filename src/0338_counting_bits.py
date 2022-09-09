from typing import *
# https://leetcode.com/problems/counting-bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n + 1):
            i_bits = 0
            while i:
                if i & 1: i_bits += 1
                i >>= 1
            result.append(i_bits)
        return result

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    def testCases(self):
        param_list = [
            (2, [0,1,1]),
            (5, [0,1,1,2,1,2]),
            (1, [0,1]),
        ]
        for n, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.countBits(n)
                # assert
                self.assertEqual(expected, result, (n))

if __name__ == '__main__':
    unittest.main()
