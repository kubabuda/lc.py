from typing import *
# https://leetcode.com/problems/sum-of-two-integers/
import math
class Solution:
    # def getSum(self, a: int, b: int) -> int:
    #     n = (2 ** a) * (2 ** b)
    #     return int(math.log(n, 2))

    def getSum(self, a: int, b: int) -> int:
        result = self.addUnsigned(a, b)
        if result > 2000: # 1000 is max input
            result_flipped_sign = 0
            for i in range(0, 32):
                mask = 1 << i
                bit = result & mask
                if not bit:
                    result_flipped_sign |= mask
            result = self.addUnsigned(result_flipped_sign, 1)
            result *= -1
        return result
    
    def addUnsigned(self, a: int, b: int) -> int:
        result = 0
        carry = 0
        for i in range(0, 32):
            mask = 1 << i
            if a & mask: carry += 1
            if b & mask: carry += 1
            if carry == 3:
                bit = 1
                carry = 1
            elif carry == 2:
                carry = 1
                bit = 0
            elif carry == 1:
                bit = 1
                carry = 0
            else:
                bit = 0
                carry = 0
            mask = bit << i
            result |= mask
        return result


import unittest

class SolutionTests(unittest.TestCase): 
    def testCases(self):
        param_list = [
            (1,2, 3),
            (1,1, 2),
            (2,3, 5),
            (0,1, 1),
            (0,-1, -1),
            (2,-3, -1),
            (-2,-3, -5),
            (-2,-2, -4),
            (-1,-1, -2),
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
