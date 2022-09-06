from typing import *

class Solution:
    def method(self):
        pass

from unittest import TestCase
import unittest

class TestTemplate(unittest.TestCase): 
    def test(self):
        # arrange
        s = Solution()
        # act
        result = 2
        # assert
        self.assertEqual(2, result)
    
    def testCases(self):
        param_list = [
            (2, 2),
        ]
        for target, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = target
                # assert
                self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
