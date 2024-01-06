from typing import *
# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        thresholds = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        values = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000 : "M",
        }
        result = []
        for t in thresholds:
            while num >= t:
                result.append(values[t])
                num -= t
        return ''.join(result)


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ]

    def testCases_intToRoman(self):
        for num, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.intToRoman(num)
                # assert
                self.assertEqual(expected, result, (num))


if __name__ == '__main__':
    unittest.main()
